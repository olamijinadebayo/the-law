from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser
import datetime as dt
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Law(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE, )
    # avatar_thumbnail = ProcessedImageField(upload_to='avatars',processors=[ResizeToFill(100, 50)],format='JPEG', options={'quality': 60})
    avatar = models.ImageField(upload_to='avatar', blank=True)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.user.username


class Lawyer(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE, related_name='lawyer_profile')
    first_name = models.CharField(max_length=60, null=True)
    last_name = models.CharField(max_length=60, null=True)
    email = models.EmailField(max_length=100)
    # bio = models.CharField(max_length=60, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    # profile_avatar = ProcessedImageField(
    #     upload_to='avatars/', processors=[ResizeToFill(100, 100)], format='JPEG', options={'quality': 60}, blank=True)
    # location = models.CharField(max_length=30, blank=True)
    # category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.user.email


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_lawyer_profile(sender, instance, created, **kwargs):
    # if instance.is_lawyer:
    if created:
        Law.objects.create(user=instance)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def save_lawyer_profile(sender, instance, **kwargs):
    # if instance.is_lawyer:
    instance.law.save()


class Articles(models.Model):
    image = ProcessedImageField(
        upload_to='posts/', processors=[ResizeToFill(700, 700)], format='JPEG', options={'quality': 100}, blank=True)
    name = models.CharField(max_length=30)
    post = models.TextField()
    time = models.DateTimeField(auto_now_add=True)
    lawyer = models.ForeignKey(Lawyer, on_delete=models.CASCADE)
