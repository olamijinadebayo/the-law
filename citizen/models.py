from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver


class Case:
    user = models.ForeignKey(User, blank=True)
    title = models.CharField(max_length=30, null=True)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
