from django.db import models

from utils.models import JSONField
from sql.problem.models import SqlProblem

from utils.shortcuts import rand_str


class JudgeSqlStatus:
    WRONG_ANSWER = -1
    ACCEPTED = 0
    RUNTIME_ERROR = 1
    SYSTEM_ERROR = 2
    PENDING = 3
    PARTIALLY_ACCEPTED = 4


class SqlSubmission(models.Model):
    id = models.TextField(default=rand_str, primary_key=True, db_index=True)
    problem = models.ForeignKey(SqlProblem, on_delete=models.CASCADE)
    create_time = models.DateTimeField(auto_now_add=True)
    user_id = models.IntegerField(db_index=True)
    username = models.TextField()
    user_queries = JSONField()  # [{ "id": 1, "query": "SELECT * FROM customers;" }]
    result = models.IntegerField(db_index=True, default=JudgeSqlStatus.PENDING)
    test_case_results = JSONField(default=list)
    # Result from JudgeServerSql
    info = JSONField(default=dict)
    shared = models.BooleanField(default=False)
    # {err_info: "", score: 0}
    statistic_info = JSONField(default=dict)
    ip = models.TextField(null=True)

    def check_user_permission(self, user, check_share=True):
        if self.user_id == user.id or user.is_super_admin() or user.can_mgmt_all_problem() or self.problem.created_by_id == user.id:
            return True

        if check_share:
            if self.problem.share_submission or self.shared:
                return True
        return False

    class Meta:
        db_table = "sql_submission"
        ordering = ("-create_time",)

    def __str__(self):
        return self.id
