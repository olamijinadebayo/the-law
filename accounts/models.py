from django.db import models
from django.contrib.auth.models import AbstractUser
# from django.db.models.signals import post_save
# from django.dispatch import receiver


class User(AbstractUser):
    is_citizen = models.BooleanField(default=False)
    is_lawyer = models.BooleanField(default=False)
