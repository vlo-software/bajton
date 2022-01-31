from django.db import models
from utils.models import RichTextField
from problem.models import Problem
from account.models import User


class ForumPost(models.Model):
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = RichTextField()
    edited = models.BooleanField(default=False)


class ForumComment(models.Model):
    post = models.ForeignKey(ForumPost, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = RichTextField()
    edited = models.BooleanField(default=False)
