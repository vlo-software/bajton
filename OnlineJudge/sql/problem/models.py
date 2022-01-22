from django.db import models
from utils.models import JSONField

from account.models import User
from utils.models import RichTextField
from utils.constants import Choices


class SqlProblemTag(models.Model):
    name = models.TextField()

    class Meta:
        db_table = "sql_problem_tag"


class SqlProblem(models.Model):
    # display ID
    _id = models.TextField(db_index=True, unique=True)
    is_public = models.BooleanField(default=False)
    title = models.TextField()
    # HTML
    description = RichTextField()
    # queries giving proper output (base64'd)
    # [{"id": 1, "query":"AEWRTFSDFG135EFG34512635 (this is base64)", "score": 10}]
    test_cases = JSONField()
    total_score = models.IntegerField(default=0)
    template = models.TextField()
    create_time = models.DateTimeField(auto_now_add=True)
    # we can not use auto_now here
    last_update_time = models.DateTimeField(null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    visible = models.BooleanField(default=True)
    tags = models.ManyToManyField(SqlProblemTag)
    source = models.TextField(null=True)
    # for OI mode
    submission_number = models.BigIntegerField(default=0)
    accepted_number = models.BigIntegerField(default=0)
    # {JudgeStatus.ACCEPTED: 3, JudgeStaus.WRONG_ANSWER: 11}, the number means count
    statistic_info = JSONField(default=dict)
    share_submission = models.BooleanField(default=False)
    # .sql dump of the problems database (B64 encoded)
    problem_data = models.TextField()

    class Meta:
        db_table = "sql_problem"
        ordering = ("create_time",)

    def add_submission_number(self):
        self.submission_number = models.F("submission_number") + 1
        self.save(update_fields=["submission_number"])

    def add_ac_number(self):
        self.accepted_number = models.F("accepted_number") + 1
        self.save(update_fields=["accepted_number"])
