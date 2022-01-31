from email.policy import default
from problem.models import Problem
from account.decorators import login_required
from forumPost.models import ForumComment, ForumPost
from forumPost.serializers import CreateOrEditForumPostSerializer, ForumPostSerializer, ForumCommentSerializer
from utils.api.api import APIView, validate_serializer


class ForumPostApi(APIView):
    @validate_serializer(CreateOrEditForumPostSerializer)
    @login_required
    def post(self, request):
        problemId = request.GET.get("problemId")
        data = request.data
        if not problemId:
            return self.error("Invalid parameter, problemId is required")
        try:
            data["problem"] = Problem.objects.get(id=problemId)
        except Problem.DoesNotExist:
            return self.error("Couldn't find a problem with a provided id")
        data["author"] = request.user
        data["edited"] = False
        try:
            forumPost = ForumPost.objects.create(**data)
        except Exception:
            return self.error("Couldn't create a new forum post")
        return self.success(ForumPostSerializer(forumPost).data)

    @login_required
    def get(self, request):
        id = request.GET.get("forumPostId")
        if not id:
            return self.error("Invalid parameter, forumPostId is required")
        try:
            post = ForumPost.objects.get(id=id)
        except ForumPost.DoesNotExist:
            return self.error("Couldn't find post")

        postWithComments = ForumPostSerializer(post).data
        postWithComments["comments"] = ForumCommentSerializer(ForumComment.objects.select_related("post").filter(post__id=id), many=True, allow_empty=True, default=[]).data

        return self.success(postWithComments)
