import random
from django.db.models import Q
from utils.api import APIView
from ..models import SqlProblem
from ..serializers import SqlProblemSerializer

# TODO: Add tag API


class SqlProblemAPI(APIView):
    @staticmethod
    def _add_problem_status(request, queryset_values):
        if request.user.is_authenticated:
            profile = request.user.userprofile
            sql_problems_status = profile.sql_problems_status.get("problems", {})
            # paginate data
            results = queryset_values.get("results")
            if results is not None:
                problems = results
            else:
                problems = [queryset_values, ]
            for problem in problems:
                problem["my_status"] = sql_problems_status.get(str(problem["id"]), {}).get("status")

    def get(self, request):
        problem_id = request.GET.get("problem_id")
        if problem_id:
            try:
                problem = SqlProblem.objects.select_related("created_by") \
                    .get(_id=problem_id, visible=True)
                problem_data = SqlProblemSerializer(problem).data
                self._add_problem_status(request, problem_data)
                return self.success(problem_data)
            except SqlProblem.DoesNotExist:
                return self.error("Problem does not exist")

        limit = request.GET.get("limit")
        if not limit:
            return self.error("limit is required")

        problems = SqlProblem.objects.select_related("created_by").filter(visible=True)

        # tag_text = request.GET.get("tag") TODO: Add tag support
        # if tag_text:
        #     problems = problems.filter(tags__name=tag_text)

        keyword = request.GET.get("keyword", "").strip()
        if keyword:
            problems = problems.filter(Q(title__icontains=keyword) | Q(_id__icontains=keyword))

        data = self.paginate_data(request, problems, SqlProblemSerializer)
        self._add_problem_status(request, data)
        return self.success(data)
