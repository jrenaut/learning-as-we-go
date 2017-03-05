from django.db import models
from podcast.models import Speaker

class Bio(models.Model):
    user = models.ForeignKey(Speaker, related_name="Speaker")
    display = models.BooleanField(default = True)
    custom_css = models.CharField(max_length=50, blank=True, null=True)

class Comment(models.Model):
    body = models.TextField()
    name = models.CharField(max_length=255)
    approved = models.BooleanField(default = False)
    email = models.EmailField()
    timestamp = models.DateTimeField(auto_now_add=True)
