import re

from django import forms

from options.options import SysOptions
from utils.api import UsernameSerializer, serializers

from .models import SqlProblem, SqlProblemTag
from .utils import parse_problem_template


class CreateTestCasesSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    query = serializers.CharField()
    score = serializers.IntegerField(min_value=0)


class CreateOrEditSqlProblemSerializer(serializers.Serializer):
    _id = serializers.CharField(max_length=32, allow_blank=True, allow_null=True)
    title = serializers.CharField(max_length=1024)
    description = serializers.CharField()
    test_cases = serializers.ListField(child=CreateTestCasesSerializer(), allow_empty=False)
    template = serializers.CharField()
    visible = serializers.BooleanField()
    tags = serializers.ListField(child=serializers.CharField(max_length=32), allow_empty=False)
    source = serializers.CharField(max_length=256, allow_blank=True, allow_null=True)
    share_submission = serializers.BooleanField()


class CreateSqlProblemSerializer(CreateOrEditSqlProblemSerializer):
    pass


class EditSqlProblemSerializer(CreateOrEditSqlProblemSerializer):
    id = serializers.IntegerField()


class SqlTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = SqlProblemTag
        fields = "__all__"


class BaseSqlProblemSerializer(serializers.ModelSerializer):
    tags = serializers.SlugRelatedField(many=True, slug_field="name", read_only=True)
    created_by = UsernameSerializer()
    template = serializers.CharField()


class SqlProblemAdminSerializer(BaseSqlProblemSerializer):
    class Meta:
        model = SqlProblem
        fields = "__all__"


class SqlProblemSerializer(BaseSqlProblemSerializer):
    class Meta:
        model = SqlProblem
        exclude = ("test_cases", "visible", "is_public", "problem_data")


class SqlProblemSafeSerializer(BaseSqlProblemSerializer):
    class Meta:
        model = SqlProblem
        exclude = ("test_cases", "visible", "is_public",
                   "submission_number", "accepted_number", "statistic_info", "problem_data")


class FormatValueSerializer(serializers.Serializer):
    format = serializers.ChoiceField(choices=["html", "markdown"])
    value = serializers.CharField(allow_blank=True)


class TestCasesSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    query = serializers.CharField()
    score = serializers.IntegerField(min_value=1)


class TemplateSerializer(serializers.Serializer):
    template = serializers.CharField()
