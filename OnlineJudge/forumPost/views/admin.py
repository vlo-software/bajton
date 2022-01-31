from forumPost.models import ForumPost
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
