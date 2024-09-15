from django.db import models
from video.models.category import Category


class Video(models.Model):
    categories = models.ManyToManyField(Category, related_name='videos')
    file = models.FileField(upload_to='videos/')
    size = models.BigIntegerField()
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file.name
