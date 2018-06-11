from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver


class User(AbstractUser):
    is_citizen = models.BooleanField(default=False)
    is_lawyer = models.BooleanField(default=False)


class CitizenProfile(models.Model):
    avatar = models.ImageField(upload_to='avatar/', blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                null=True, related_name='citizen_profile')
    email = models.EmailField(max_length=50, null=True)
    first_name = models.CharField(max_length=30, null=True)
    last_name = models.CharField(max_length=30, null=True)


class LawyerProfile(models.Model):
    avatar = models.ImageField(upload_to='logo/', blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                null=True, related_name='lawyer_profile')
    email = models.EmailField(max_length=50, null=True)
    first_name = models.CharField(max_length=30, null=True)
    last_name = models.CharField(max_length=30, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    articles = models.ForeignKey(Articles, on_delete=models.CASCADE)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if instance.is_citizen:
        CitizenProfile.objects.get_or_create(user=instance)
    else:
        LawyerProfile.objects.get_or_create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    if instance.is_citizen:
        instance.citizen_profile.save()
    else:
        LawyerProfile.objects.get_or_create(user=instance)
