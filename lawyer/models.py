from django.db import models

# Create your models here.
class User(AbstractUser):
    is_lawyer = models.BooleanField(default=False)
    