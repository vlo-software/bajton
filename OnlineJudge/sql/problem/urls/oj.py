
from django.conf.urls import url

from ..views.oj import SqlProblemAPI

urlpatterns = [
    url(r"^sqlproblem/?$", SqlProblemAPI.as_view(), name="sql_problem_api")
]
