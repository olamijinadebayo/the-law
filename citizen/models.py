from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # avatar_thumbnail = ProcessedImageField(upload_to='avatars',processors=[ResizeToFill(100, 50)],format='JPEG', options={'quality': 60})
    avatar = models.ImageField(upload_to='avatar', blank=True)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.user.username

        

class Citizen(models.Model):
    '''
    creating a profile model for each citizen
    '''
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE, related_name='citizen_profile')
    first_name = models.CharField(max_length=30, null=True)
    last_name = models.CharField(max_length=30, null=True)

    def __str__(self):
        return self.user


class Post(models.Model):
    PRIMARY='pr'
    CASE_CATEGORY = (
        (PRIMARY, 'None'),
        ('Dd', 'Druken disorder'),
        ('Lf', 'Land fraud'),
        ('Rb', 'Robbery'),
        ('Md', 'Murder'),
        ('Fr', 'Fraud'),
        ('Sa', 'Sexual Assault'),
    )
    case_category = models.CharField(
        max_length=2,
        choices=CASE_CATEGORY,
        default=PRIMARY,
    )
    # case_category = models.CharField(max_length=30)
    case_number = models.CharField(max_length=12)
    case_description = models.TextField()
    post_date = models.DateTimeField(auto_now_add=True)
    citizen = models.ForeignKey(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)


    def __str__(self):
        return self.case_description



@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
