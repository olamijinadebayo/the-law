from django.contrib.gis.db import models
from django.conf import settings
from django.core.urlresolvers import reverse
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser
import datetime as dt
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from citizen.models import Profile,Citizen
from phonenumber_field.modelfields import PhoneNumberField
import citizen
# Create your model

class Lawyer(models.Model):
    GENERAL = 'GN'
    LAW_CATEGORIES = (
        ('CL','Criminal'),
        ('CE','Corporate'),
        ('FL','Financial'),
        ('ET','Entertainment'),
        ('FY','Family'),
        ('EL','Enviromental'),
        ('AY','Admiralty'),
        (GENERAL,'General'),
    )
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE,null=True, related_name='lawyer_profile')
    first_name = models.CharField(max_length=60, null=True)
    last_name = models.CharField(max_length=60, null=True)
    email = models.EmailField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    avatar = models.ImageField(upload_to='avatar', blank=True)
    bio = models.TextField(max_length=500, blank=True)
    location = models.PointField(srid=4326, null=True)
    phone = PhoneNumberField(null=True, blank=True)
    objects =  models.GeoManager()
    category = models.CharField(max_length=20,choices = LAW_CATEGORIES,default=GENERAL,)

    def __str__(self):
        return self.user.username

    @receiver(post_save, sender=settings.AUTH_USER_MODEL)
    def create_lawyer_profile(sender, instance, created, **kwargs):
        if created:
            if instance.is_lawyer:
                Lawyer.objects.create(user=instance)
            else:
                citizen.models.Profile.objects.create(user=instance)

    @receiver(post_save, sender=settings.AUTH_USER_MODEL)
    def save_lawyer_profile(sender, instance, **kwargs):
        if instance.is_lawyer:
            instance.lawyer_profile.save()
        else:
            instance.citizen_info.save()

class AllLawyer(models.Model):
    name = models.CharField(max_length=250)
    icon = models.CharField(max_length=250)
    description = models.CharField(max_length=250)

    geom = models.PointField(srid=4326)
    objects = models.GeoManager()


class Articles(models.Model):
    image = ProcessedImageField(
        upload_to='posts/', processors=[ResizeToFill(700, 700)], format='JPEG', options={'quality': 100}, blank=True)
    name = models.CharField(max_length=30)
    post = models.TextField()
    time = models.DateTimeField(auto_now_add=True)
    lawyer = models.ForeignKey(Lawyer, on_delete=models.CASCADE)
