import hashlib
import json
import os
# import shutil
import tempfile
import zipfile
from wsgiref.util import FileWrapper

from django.conf import settings
from django.db import transaction
from django.db.models import Q
from django.http import StreamingHttpResponse, FileResponse

from account.decorators import problem_permission_required, ensure_created_by
from contest.models import Contest, ContestStatus
from fps.parser import FPSHelper, FPSParser
from judge.dispatcher import SPJCompiler
from options.options import SysOptions
from submission.models import Submission, JudgeStatus
from utils.api import APIView, CSRFExemptAPIView, validate_serializer, APIError
from utils.constants import Difficulty
from utils.shortcuts import rand_str, natural_sort_key
from utils.tasks import delete_files
from ..models import SqlProblem, SqlProblemTag
from ..serializers import (CreateSqlProblemSerializer, EditSqlProblemSerializer, SqlProblemAdminSerializer)
from ..utils import (TEMPLATE_BASE, build_problem_template)


class SqlProblemApi(APIView):
    @problem_permission_required
    @validate_serializer(CreateSqlProblemSerializer)
    def post(self, request):
        data = request.data
        _id = data["_id"]
        if not _id:
            return self.error("Display ID is required")
        if SqlProblem.objects.filter(_id=_id).exists():
            return self.error("Display ID already exists")

        # calculating the total score for the problem
        total_score = 0
        for item in data["test_cases"]:
            if item["score"] <= 0:
                return "Invalid score"
            else:
                total_score += item["score"]
        data["total_score"] = total_score

        tags = data.pop("tags")
        data["created_by"] = request.user
        problem = SqlProblem.objects.create(**data)

        for item in tags:
            try:
                tag = SqlProblemTag.objects.get(name=item)
            except SqlProblemTag.DoesNotExist:
                tag = SqlProblemTag.objects.create(name=item)
            problem.tags.add(tag)
        return self.success(SqlProblemAdminSerializer(problem).data)

    @problem_permission_required
    def get(self, request):
        problem_id = request.GET.get("id")
        user = request.user
        if problem_id:
            try:
                problem = SqlProblem.objects.get(id=problem_id)
                ensure_created_by(problem, user)
                return self.success(SqlProblemAdminSerializer(problem).data)
            except SqlProblem.DoesNotExist:
                return self.error("Problem does not exist")
        problems = SqlProblem.objects.order_by("-create_time")
        keyword = request.GET.get("keyword", "").strip()
        if keyword:
            problems = problems.filter(Q(title__icontains=keyword) | Q(_id__icontains=keyword))
        if not user.can_mgmt_all_problem():
            problems = problems.filter(created_by=user)
        return self.success(self.paginate_data(request, problems, SqlProblemAdminSerializer))
