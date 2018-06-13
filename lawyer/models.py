from django.db import models
from django.contrib.auth.models import AbstractUser
import datetime as dt
from django.contrib.auth.models import User
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from django.conf import settings
# Create your models here.


class Articles(models.Model):
    image = ProcessedImageField(upload_to = 'posts/', processors=[ResizeToFill(700,700)], format = 'JPEG', options ={'quality':100}, blank=True)
    name = models.CharField(max_length=30)
    post = models.TextField()
    time = models.DateTimeField(auto_now_add=True)
    user_name = models.ForeignKey(settings.AUTH_USER_MODEL)

class Category(models.Model):
    name = models.CharField(max_length=30)
user_name = models.ForeignKey(settings.AUTH_USER_MODEL)
    

class Lawyer(models.Model):
    user_name = models.OneToOneField(settings.AUTH_USER_MODEL)
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    email = models.EmailField(max_length=100)
    bio = models.CharField(max_length=60, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    profile_avatar = ProcessedImageField(upload_to = 'avatars/', processors=[ResizeToFill(100,100)], format = 'JPEG', options ={'quality':60})
    location = models.CharField(max_length=30,blank=True)

