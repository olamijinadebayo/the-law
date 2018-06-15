from django.conf.urls import url
from . import views
import lawyer

app_name = 'citizen'

urlpatterns = [
    url(r'^post/$', views.post, name='post'),
    url(r'^profile/', views.profile_edit, name='edit'),
]