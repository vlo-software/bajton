from forumPost.models import ForumComment, ForumPost
from account.decorators import super_admin_required
from utils.api import APIView


class ForumPostApi(APIView):
    @super_admin_required
    def delete(self, request):
        id = request.GET.get("id")
        if not id:
            return self.error("Invalid parameter, id is required")
        try:
            post = ForumPost.objects.get(id=id)
        except ForumPost.DoesNotExist:
            return self.error("Post does not exist")
        post.delete()
        return self.success()


class ForumCommentApi(APIView):
    @super_admin_required
    def delete(self, request):
        id = request.GET.get("id")
        if not id:
            return self.error("Invalid parameter, id is required")
        try:
            comment = ForumComment.objects.get(id=id)
        except ForumComment.DoesNotExist:
            return self.error("Comment does not exist")
        comment.delete()
        return self.success()
