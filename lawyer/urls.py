from django.conf.urls import url, include
from .import views 

urlpatterns = [
    url(r'lawyer/$', views.lawyerdashboard, name= 'lawyerdashboard'),
    url(r'lawyer/profile/', views.lawyerprofile, name = 'lawyerprofile'),
    url(r'lawyer/cases/', views.lawyercases, name = 'lawyercases'),
    url(r'lawyer/new/article', views.newarticle, name = 'newarticle'),
    url(r'lawyer/change_lawyerProfile/(\d+)$', views.change_lawyerProfile, name='change_lawyerProfile'),
]