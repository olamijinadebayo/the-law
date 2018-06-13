<<<<<<< HEAD
from django.db import models

# Create your models here.
class Post(models.Model):
    case_category = models.CharField(max_length=30)
    case_number = models.CharField(max_length=12)
    case_description = models.TextField()
    post_date = models.DateTimeField(auto_now_add=True)

=======
>>>>>>> 23948793bf8e60a57df830f5ffb4fe1d45faf7d2
