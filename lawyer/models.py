from django.db import models
from django.conf import settings


class Lawyer(models.Model):
    '''
    creating a profile model for each citizen
    '''
    avatar = models.ImageField(upload_to='lawyer_avatar/', blank=True)
    bio = models.TextField()
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE, related_name='lawyer_profile')
    first_name = models.CharField(max_length=30, null=True)
    last_name = models.CharField(max_length=30, null=True)
    location = models.CharField(max_length=30, null=True)

    @receiver(post_save, sender=User)
    def update_user_profile(sender, instance, created, **kwargs):
        if created:
            Lawyer.objects.create(user=instance)
        instance.lawyer.save()
