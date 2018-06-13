from django.db import models
from django.conf import settings


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
