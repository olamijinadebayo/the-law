from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class Articles(models.Model):
    image = ProcessedImageField(upload_to = 'posts/', processors=[ResizeToFill(700,700)], format = 'JPEG', options ={'quality':100})
    name = models.CharField(max_length=30)
    post = models.TextField()
    time = models.DateTimeField(auto_now_add=True)
    