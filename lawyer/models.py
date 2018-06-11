from django.db import models
from django.contrib.auth.models import AbstractUser
import datetime as dt
from django.contrib.auth.models import User
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
# Create your models here.


class Articles(models.Model):
    image = ProcessedImageField(upload_to = 'posts/', processors=[ResizeToFill(700,700)], format = 'JPEG', options ={'quality':100}, blank=True)
    name = models.CharField(max_length=30)
    post = models.TextField()
    time = models.DateTimeField(auto_now_add=True)
    user_name = models.ForeignKey(User, on_delete=models.CASCADE)

class Category(models.Model):
    name = models.CharField(max_length=30)
    user_name = models.ForeignKey(User, on_delete=models.CASCADE)
    