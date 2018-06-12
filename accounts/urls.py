from django.conf.urls import url
from . import views
from django.conf import settings

app_name='accounts'

urlpatterns = [
    url(r'^home/$', views.home, name='home'),
    url(r'^citizensignup/$', views.citizensignup, name='citizen'),
    url(r'^lawyersignup/$', views.lawyer_signup, name='lawyer'),
]
