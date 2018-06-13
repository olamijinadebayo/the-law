from django.conf.urls import url
from . import views
from django.conf import settings

urlpatterns = [
    url(r'^citizen/$', views.citizen, name='citizen'),
    url(r'^lawyer/$', views.lawyer, name='lawyer'),
    url(r'^loginpage/$', views.loginpage, name='loginpage'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^citizensignup/$', views.citizensignup, name='citizen'),
    url(r'^lawyersignup/$', views.lawyersignup, name='lawyer'),
]
