from email.policy import default
from problem.models import Problem
from account.decorators import login_required
from forumPost.models import ForumComment, ForumPost
from forumPost.serializers import CreateOrEditForumCommentSerializer, CreateOrEditForumPostSerializer, ForumPostSerializer, ForumCommentSerializer
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

    @validate_serializer(CreateOrEditForumPostSerializer)
    @login_required
    def put(self, request):
        data = request.data
        id = request.GET.get("forumPostId")
        if not id:
            return self.error("Invalid parameter, forumPostId is required")

        try:
            post = ForumPost.objects.get(id=id)
        except ForumPost.DoesNotExist:
            return self.error("Couldn't find post")

        setattr(post, "content", data["content"])
        setattr(post, "edited", True)

        try:
            post.save()
        except Exception:
            return self.error("Couldn't update the forum post")
        return self.success()

    @login_required
    def get(self, request):
        id = request.GET.get("forumPostId")
        problemId = request.GET.get("problemId")
        if not id and not problemId:
            return self.error("Invalid parameter, forumPostId or problemId is required")
        try:
            db_data = ForumPost.objects.get(id=id) if id else ForumPost.objects.filter(problem_id=problemId)
        except ForumPost.DoesNotExist:
            return self.error("Couldn't find post")

        if id:
            postWithComments = ForumPostSerializer(db_data).data
            postWithComments["comments"] = ForumCommentSerializer(ForumComment.objects.select_related("post").filter(post__id=id), many=True, allow_empty=True, default=[]).data

            return self.success(postWithComments)
        else:
            posts = []
            for post in db_data:
                postWithComments = ForumPostSerializer(post).data
                postWithComments["comments"] = ForumCommentSerializer(ForumComment.objects.select_related(
                    "post").filter(post__id=post.id), many=True, allow_empty=True, default=[]).data
                posts.append(postWithComments)
            return self.success(posts)


class ForumCommentApi(APIView):
    @validate_serializer(CreateOrEditForumCommentSerializer)
    @login_required
    def post(self, request):
        postId = request.GET.get("forumPostId")
        data = request.data
        if not postId:
            return self.error("Invalid parameter, forumPostId is required")
        try:
            data["post"] = ForumPost.objects.get(id=postId)
        except Problem.DoesNotExist:
            return self.error("Couldn't find a forum post with a provided id")
        data["author"] = request.user
        data["edited"] = False
        try:
            forumComment = ForumComment.objects.create(**data)
        except Exception:
            return self.error("Couldn't create a new comment")
        return self.success(ForumCommentSerializer(forumComment).data)

    @validate_serializer(CreateOrEditForumCommentSerializer)
    @login_required
    def put(self, request):
        commentId = request.GET.get("commentId")
        data = request.data
        if not commentId:
            return self.error("Invalid parameter, commentId is required")
        try:
            comment = ForumComment.objects.get(id=commentId)
        except Problem.DoesNotExist:
            return self.error("Couldn't find a forum comment with a provided id")

        setattr(comment, "content", data["content"])
        setattr(comment, "edited", True)

        try:
            comment.save()
        except Exception:
            return self.error("Couldn't update the comment")
        return self.success()
