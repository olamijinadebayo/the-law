from django.contrib import admin
from .models import Lawyer, Articles, Category, Law
admin.site.register(Lawyer)
admin.site.register(Articles)
admin.site.register(Category)
admin.site.register(Law)
