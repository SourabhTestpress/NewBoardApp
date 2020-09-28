from django.db import models
from django.conf import settings
from django.urls import reverse
from model_utils.models import TimeStampedModel


class Board(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True)
    description = models.TextField(max_length=500)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("detail", args=(self.slug,))


class Topic(models.Model):
    board = models.ForeignKey("Board", on_delete=models.CASCADE, related_name="topics")
    slug = models.SlugField(unique=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="topics"
    )
    subject = models.CharField(max_length=100)
    last_updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject

    def get_absolute_url(self):
        return reverse("get_topic_detail", args=(self.slug,))


class Post(TimeStampedModel):
    topic = models.ForeignKey("Topic", on_delete=models.CASCADE, related_name="posts")
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="posts"
    )
    updated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, related_name="+"
    )
    message = models.TextField(max_length=2000)

    def __str__(self):
        return str(self.message)[:20]
