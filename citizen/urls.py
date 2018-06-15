from django.conf.urls import url
from . import views
import lawyer

app_name = 'citizen'

urlpatterns = [
    url(r'', views.post, name='post'),
]