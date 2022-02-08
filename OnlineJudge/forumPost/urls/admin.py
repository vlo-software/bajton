from django.conf.urls import url

from ..views.admin import ForumPostApi, ForumCommentApi

urlpatterns = [
    url(r"^post/?$", ForumPostApi.as_view(), name="forum_post_admin_api"),
    url(r"^comment/?$", ForumCommentApi.as_view(), name="forum_comment_admin_api")
]
