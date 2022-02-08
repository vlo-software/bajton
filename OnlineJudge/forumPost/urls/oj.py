from django.conf.urls import url

from ..views.oj import ForumPostApi, ForumCommentApi

urlpatterns = [
    url(r"^post/?$", ForumPostApi.as_view(), name="forum_post_api"),
    url(r"^comment/?$", ForumCommentApi.as_view(), name="forum_comment_api"),
]
