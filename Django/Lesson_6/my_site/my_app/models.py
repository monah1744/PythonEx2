from django.contrib.auth.models import AbstractUser
from django.db import models


class PortalUser(AbstractUser):
    def __str__(self):
        return "{}".format(self.username)

    username = models.CharField(max_length=20, unique=True)
    firsrt_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    is_moderator = models.BooleanField(default=False)


class Article(models.Model):
    def __str__(self):
        return "{}".format(self.title)

    title = models.CharField(max_length=80)
    text = models.TextField()
    author = models.ForeignKey(
        PortalUser, on_delete=models.SET_NULL, blank=True, null=True)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)
    source = models.ForeignKey(
        'Source', on_delete=models.CASCADE, blank=True, null=True)


class LikeandComment(models.Model):
    class Meta:
        abstract = True
    user = models.ForeignKey(
        PortalUser, on_delete=models.SET_NULL, blank=True, null=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)


class Like(LikeandComment):
    pass


class Comment(LikeandComment):
    text = models.TextField()


class Source(models.Model):
    PUBLISHERS = [
        (1, 'BBC'),
        (2, 'CNN'),
        (3, 'Ukraine news')
    ]
    name = models.PositiveIntegerField(choices=PUBLISHERS, unique=True)


class Tag(models.Model):
    name = models.CharField(max_length=80)
    articles = models.ManyToManyField(Article)
    parent_tag = models.ForeignKey('Tag', on_delete=models.CASCADE)
