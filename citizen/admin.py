from django.contrib import admin
from .models import Citizen, Profile,Post
# Register your models here.
admin.site.register(Citizen)
admin.site.register(Profile)
admin.site.register(Post)
