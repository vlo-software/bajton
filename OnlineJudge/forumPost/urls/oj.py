from django.conf.urls import url

from ..views.oj import ForumPostApi

urlpatterns = [
    url(r"^post/?$", ForumPostApi.as_view(), name="forum_post_api"),
]
