from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Citizen(models.Model):
    '''
    creating a profile model for each citizen
    '''
    avatar = models.ImageField(upload_to='avatar/', blank=True)
    bio = models.TextField()
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE, related_name='citizen_profile')
    first_name = models.CharField(max_length=30, null=True)
    last_name = models.CharField(max_length=30, null=True)

    def __str__(self):
        return self.user


class Post(models.Model):
    case_category = models.CharField(max_length=30)
    case_number = models.CharField(max_length=12)
    case_description = models.TextField()
    post_date = models.DateTimeField(auto_now_add=True)
    citizen = models.ForeignKey(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)
