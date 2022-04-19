from django.db.models import Q

from account.decorators import problem_permission_required, ensure_created_by
from utils.api import APIView, validate_serializer
from ..models import SqlProblem
from ..serializers import (CreateSqlProblemSerializer, EditSqlProblemSerializer, SqlProblemAdminSerializer)
import base64


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
            if item["score"] < 10:
                return "Invalid score (min 10)"
            elif item["score"] > 100:
                return "Invalid score (max 100)"
            else:
                total_score += item["score"]
        data["total_score"] = total_score

        # tags = data.pop("tags") # TODO: support tags
        data["created_by"] = request.user
        data["problem_data"] = str(base64.b64encode(data["problem_data"].encode("utf-8")), encoding='utf-8')  # The database is stored as base64
        data["test_cases"] = list(map(lambda t: {"id": t["id"], "score": t["score"], "query": str(base64.b64encode(
            t["query"].encode("utf-8")), encoding='utf-8')}, data["test_cases"]))  # The queries are stored as base64
        problem = SqlProblem.objects.create(**data)

        # for item in tags: # TODO: support tags
        #     try:
        #         tag = SqlProblemTag.objects.get(name=item)
        #     except SqlProblemTag.DoesNotExist:
        #         tag = SqlProblemTag.objects.create(name=item)
        #     problem.tags.add(tag)
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

    @problem_permission_required
    @validate_serializer(EditSqlProblemSerializer)
    def put(self, request):  # TODO: Test this
        data = request.data
        problem_id = data.pop("id")

        try:
            problem = SqlProblem.objects.get(id=problem_id)
            ensure_created_by(problem, request.user)
        except SqlProblem.DoesNotExist:
            return self.error("Problem does not exist")

        _id = data["_id"]
        if not _id:
            return self.error("Display ID is required")
        if SqlProblem.objects.exclude(id=problem_id).filter(_id=_id).exists():
            return self.error("Display ID already exists")

        error_info = self.common_checks(request)  # TODO: add common checks
        if error_info:
            return self.error(error_info)
        # tags = data.pop("tags") # TODO: support tags

        # calculating the total score for the problem
        total_score = 0
        for item in data["test_cases"]:
            if item["score"] < 10:
                return "Invalid score (min 10)"
            elif item["score"] > 100:
                return "Invalid score (max 100)"
            else:
                total_score += item["score"]

        data["total_score"] = total_score
        data["problem_data"] = str(base64.b64encode(data["problem_data"].encode("utf-8")), encoding='utf-8')  # The database is stored as base64
        data["test_cases"] = list(map(lambda t: {"id": t["id"], "score": t["score"], "query": str(base64.b64encode(
            t["query"].encode("utf-8")), encoding='utf-8')}, data["test_cases"]))

        for k, v in data.items():
            setattr(problem, k, v)
        problem.save()

        # problem.tags.remove(*problem.tags.all()) # TODO: support tags
        # for tag in tags:
        #     try:
        #         tag = ProblemTag.objects.get(name=tag)
        #     except ProblemTag.DoesNotExist:
        #         tag = ProblemTag.objects.create(name=tag)
        #     problem.tags.add(tag)

        return self.success()

    @problem_permission_required
    def delete(self, request):
        id = request.GET.get("id")
        if not id:
            return self.error("Invalid parameter, id is required")
        try:
            problem = SqlProblem.objects.get(id=id)
        except SqlProblem.DoesNotExist:
            return self.error("Problem does not exists")
        ensure_created_by(problem, request.user)
        problem.delete()
        return self.success()
