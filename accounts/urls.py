from django.conf.urls import url
# from django.contrib.auth.views import view as auth_view
from . import views
from django.conf import settings

app_name='accounts'

urlpatterns = [
    url(r'^home/$', views.home, name='home'),
    url(r'^citizen/signup/$', views.citizensignup, name='citizen'),
    url(r'^lawyer/signup/$', views.lawyer_signup, name='lawyer'),
]
