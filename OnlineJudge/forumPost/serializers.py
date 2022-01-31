from email.policy import default
from django import forms

from utils.api import serializers, UsernameSerializer


class CreateOrEditForumPostSerializer(serializers.Serializer):
    content = serializers.CharField()


class CreateOrEditForumCommentSerializer(serializers.Serializer):
    content = serializers.CharField()


class ForumCommentSerializer(serializers.Serializer):
    content = serializers.CharField()
    author = UsernameSerializer()
    edited = serializers.BooleanField()


class ForumPostSerializer(serializers.Serializer):
    content = serializers.CharField()
    author = UsernameSerializer()
    edited = serializers.BooleanField()
