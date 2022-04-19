from account.decorators import login_required
from judgeSql.tasks import addJob
from options.options import SysOptions
from sql.problem.models import SqlProblem
from utils.api import APIView, validate_serializer
from utils.cache import cache
from utils.captcha import Captcha
from utils.throttling import TokenBucket
from ..models import SqlSubmission
from ..serializers import (CreateSqlSubmissionSerializer, SqlSubmissionModelSerializer,
                           ShareSqlSubmissionSerializer)
from ..serializers import SqlSubmissionListSerializer
import base64


class SqlSubmissionAPI(APIView):
    def throttling(self, request):
        # 使用 open_api 的请求暂不做限制
        auth_method = getattr(request, "auth_method", "")
        if auth_method == "api_key":
            return
        user_bucket = TokenBucket(key=str(request.user.id),
                                  redis_conn=cache, **SysOptions.throttling["user"])
        can_consume, wait = user_bucket.consume()
        if not can_consume:
            return "Please wait %d seconds" % (int(wait))

        # ip_bucket = TokenBucket(key=request.session["ip"],
        #                         redis_conn=cache, **SysOptions.throttling["ip"])
        # can_consume, wait = ip_bucket.consume()
        # if not can_consume:
        #     return "Captcha is required"

    @validate_serializer(CreateSqlSubmissionSerializer)
    @login_required
    def post(self, request):
        data = request.data

        if data.get("captcha"):
            if not Captcha(request).check(data["captcha"]):
                return self.error("Invalid captcha")
        error = self.throttling(request)
        if error:
            return self.error(error)

        try:
            problem = SqlProblem.objects.get(id=data["problem_id"], visible=True)
        except SqlProblem.DoesNotExist:
            return self.error("Problem not exist")
        data["user_queries"] = list(map(lambda q: {"id": q["id"], "query": str(base64.b64encode(q["query"].encode("utf-8")), encoding="utf-8")}, data["user_queries"]))
        submission = SqlSubmission.objects.create(user_id=request.user.id,
                                                  username=request.user.username,
                                                  user_queries=data["user_queries"],
                                                  problem_id=problem.id,
                                                  ip=request.session["ip"])

        if len(submission.user_queries) != len(problem.test_cases):
            return self.error("The number of queries is not equal to the number of test cases")

        tests = list(map(lambda t: {"id": t["id"], "testQuery": t["query"], "userQuery": list(
            filter(lambda q: q["id"] == t["id"], submission.user_queries))[0]["query"]}, problem.test_cases))

        addJob(submission.id, problem.problem_data, tests)

        return self.success({"submission_id": submission.id})

    @login_required
    def get(self, request):
        submission_id = request.GET.get("id")
        if not submission_id:
            return self.error("Parameter id doesn't exist")
        try:
            submission = SqlSubmission.objects.select_related("problem").get(id=submission_id)
        except SqlSubmission.DoesNotExist:
            return self.error("Submission doesn't exist")
        if not submission.check_user_permission(request.user):
            return self.error("No permission for this submission")

        submission_data = SqlSubmissionModelSerializer(submission).data
        # 是否有权限取消共享
        submission_data["can_unshare"] = submission.check_user_permission(request.user, check_share=False)
        return self.success(submission_data)

    @validate_serializer(ShareSqlSubmissionSerializer)
    @login_required
    def put(self, request):  # The id should probably be a URL parameter, but that's how it works in other endpoints (legacy code ey!?)
        """
        share submission
        """
        try:
            submission = SqlSubmission.objects.select_related("problem").get(id=request.data["id"])
        except SqlSubmission.DoesNotExist:
            return self.error("Submission doesn't exist")
        if not submission.check_user_permission(request.user, check_share=False):
            return self.error("No permission to share the submission")
        submission.shared = request.data["shared"]
        submission.save(update_fields=["shared"])
        return self.success()


class SqlSubmissionListAPI(APIView):
    def get(self, request):
        if not request.GET.get("limit"):
            return self.error("Limit is needed")

        submissions = SqlSubmission.objects.select_related("problem__created_by")
        problem_id = request.GET.get("problem_id")
        myself = request.GET.get("myself")
        result = request.GET.get("result")
        username = request.GET.get("username")
        if problem_id:
            try:
                problem = SqlProblem.objects.get(_id=problem_id, visible=True)
            except SqlProblem.DoesNotExist:
                return self.error("Problem doesn't exist")
            submissions = submissions.filter(problem=problem)
        if (myself and myself == "1") or not SysOptions.submission_list_show_all:
            submissions = submissions.filter(user_id=request.user.id)
        elif username:
            submissions = submissions.filter(username__icontains=username)
        if result:
            submissions = submissions.filter(result=result)
        data = self.paginate_data(request, submissions)
        data["results"] = SqlSubmissionListSerializer(data["results"], many=True, user=request.user).data
        return self.success(data)


class SqlSubmissionExistsAPI(APIView):  # This endpoint failes if the id is not an integer (TODO: Fix this)
    def get(self, request):
        if not request.GET.get("problem_id"):
            return self.error("Parameter error, problem_id is required")
        return self.success(request.user.is_authenticated and
                            SqlSubmission.objects.filter(problem_id=request.GET["problem_id"],
                                                         user_id=request.user.id).exists())
