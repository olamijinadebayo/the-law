from django.conf.urls import url
from . import views
from django.conf import settings

urlpatterns = [
    url(r'^home/$', views.home, name='home'),
    url(r'^citizensignup/$', views.citizensignup, name='citizen'),
    url(r'^lawyersignup/$', views.lawyersignup, name='lawyer'),
]
