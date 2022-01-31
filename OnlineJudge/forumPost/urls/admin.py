from django.conf.urls import url

from ..views.admin import ForumPostApi

urlpatterns = [
    url(r"^post/?$", ForumPostApi.as_view(), name="forum_post_admin_api")
]
