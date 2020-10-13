from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Video(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    title = models.CharField(max_length = 100)
    description = models.TextField(max_length = 1000, blank = True)
    path = models.FileField(upload_to = 'videos/')
    date_created = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    video = models.ForeignKey(Video, on_delete = models.CASCADE)
    text = models.TextField(max_length = 300)
    date_created = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.text

