from django.conf.urls import url, include
from .import views 

urlpatterns = [
    url(r'lawyer/$', views.lawyerdashboard, name= 'lawyerdashboard'),
    url(r'lawyer/profile/', views.lawyerprofile,name = 'lawyerprofile'),
]