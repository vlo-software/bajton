from typing import List, Dict
import redis
from oj.settings import REDIS_URL
import json
from sql.submission.models import SqlSubmission, JudgeSqlStatus
import time
import dramatiq

r = redis.from_url(url=REDIS_URL)
p = r.pubsub()


def addJob(submission_id: str, database: str, tests: List[Dict]) -> None:
    data = {
        "submissionId": submission_id,
        "database": database,
        "tests": tests
    }
    receivers = r.publish("judge-server-sql-jobs", json.dumps(data))
    if receivers == 0:
        SqlSubmission.objects.filter(id=submission_id).update(status=JudgeSqlStatus.SYSTEM_ERROR)


@dramatiq.actor
def listenForResults() -> None:  # This has to be run with dramatiq worker, because it is blocking
    r = redis.from_url(url=REDIS_URL)
    while True:
        message = r.rpop("judge-server-sql-results")  # None if there is no message
        if message:
            data = json.loads(message)
            submission = SqlSubmission.objects.select_related("problem").get(id=data["submissionId"])
            if not submission:
                raise Exception("Submission not found")
            submission.info = data
            passed = 0
            failed = 0
            errored = 0
            err_info = ""
            for test in data["results"]:
                if test["result"] == "passed":
                    passed += 1
                elif test["result"] == "failed":
                    failed += 1
                elif test["result"] == "error":
                    errored += 1
                    err_info += str(test["id"]) + test["userOutput"] + "\n"
            if passed == len(data["results"]):
                submission.result = JudgeSqlStatus.ACCEPTED
            elif failed == len(data["results"]):
                submission.result = JudgeSqlStatus.WRONG_ANSWER
            elif passed > 0:
                submission.result = JudgeSqlStatus.PARTIALLY_ACCEPTED
            elif errored != 0:
                submission.result = JudgeSqlStatus.RUNTIME_ERROR
            submission.test_case_results = list(map(lambda t: {"id": t["id"], "result": t["result"]}, data["results"]))
            test_cases = submission.problem.test_cases
            score = 0
            for test in data["results"]:
                if test["result"] == "passed":
                    score += list(filter(lambda t: t["id"] == test["id"], test_cases))[0]["score"]
            submission.statistic_info = {
                "err_info": err_info,
                "score": score
            }
            submission.save(update_fields=["result", "statistic_info", "info", "test_case_results"])
            submission.problem.add_submission_number()
            if submission.result == JudgeSqlStatus.ACCEPTED:
                submission.problem.add_ac_number()
        else:
            time.sleep(1)  # if there are no messages wait for a second


p.subscribe("judge-server-sql-results")
listenForResults.send()
