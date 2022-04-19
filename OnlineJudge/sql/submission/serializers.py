from .models import SqlSubmission
from utils.api import serializers


class CreateUserQuerySerializer(serializers.Serializer):
    id = serializers.IntegerField()
    query = serializers.CharField()


class CreateSqlSubmissionSerializer(serializers.Serializer):
    problem_id = serializers.IntegerField()
    user_queries = serializers.ListField(child=CreateUserQuerySerializer(), allow_empty=False)
    captcha = serializers.CharField(required=False)


class ShareSqlSubmissionSerializer(serializers.Serializer):
    id = serializers.CharField()
    shared = serializers.BooleanField()


class SqlSubmissionModelSerializer(serializers.ModelSerializer):
    problem = serializers.SlugRelatedField(read_only=True, slug_field="_id")

    class Meta:
        model = SqlSubmission
        exclude = ("info",)  # Info contains the test queries, which cannot be seen by the user.


class SqlSubmissionListSerializer(serializers.ModelSerializer):
    problem = serializers.SlugRelatedField(read_only=True, slug_field="_id")
    show_link = serializers.SerializerMethodField()

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop("user", None)
        super().__init__(*args, **kwargs)

    class Meta:
        model = SqlSubmission
        exclude = ("info", "user_queries", "ip")

    def get_show_link(self, obj):
        # 没传user或为匿名user
        if self.user is None or not self.user.is_authenticated:
            return False
        return obj.check_user_permission(self.user)
