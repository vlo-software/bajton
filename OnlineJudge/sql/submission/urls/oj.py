from django.conf.urls import url

from ..views.oj import SqlSubmissionAPI, SqlSubmissionListAPI, SqlSubmissionExistsAPI

urlpatterns = [
    url(r"^sqlsubmission/?$", SqlSubmissionAPI.as_view(), name="sqlsubmission_api"),
    url(r"^sqlsubmissions/?$", SqlSubmissionListAPI.as_view(), name="sqlsubmission_list_api"),
    url(r"^sqlsubmission_exists/?$", SqlSubmissionExistsAPI.as_view(), name="sqlsubmission_exists"),
]
