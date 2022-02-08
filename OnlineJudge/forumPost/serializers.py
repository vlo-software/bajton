from utils.api import serializers, UsernameSerializer


class CreateOrEditForumPostSerializer(serializers.Serializer):
    content = serializers.CharField()


class CreateOrEditForumCommentSerializer(serializers.Serializer):
    content = serializers.CharField()


class ForumCommentSerializer(serializers.Serializer):
    content = serializers.CharField()
    author = UsernameSerializer()
    edited = serializers.BooleanField()
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()
    id = serializers.IntegerField()


class ForumPostSerializer(serializers.Serializer):
    content = serializers.CharField()
    author = UsernameSerializer()
    edited = serializers.BooleanField()
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()
    id = serializers.IntegerField()
