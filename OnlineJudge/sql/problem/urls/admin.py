from django.conf.urls import url

from ..views.admin import SqlProblemApi

urlpatterns = [
    url(r"^sqlproblem/?$", SqlProblemApi.as_view(), name="sql_problem_admin_api")
]
