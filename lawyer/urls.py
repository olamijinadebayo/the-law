from django.conf.urls import url, include
from .import views

app_name = 'lawyer'

urlpatterns = [
    url(r'^$', views.lawyerdashboard, name='lawyerdashboard'),
    url(r'^profile/(\d+)/$', views.lawyerprofile, name='lawyerprofile'),
    url(r'cases/', views.lawyercases, name='lawyercases'),
    url(r'new/article', views.newarticle, name='newarticle'),
    url(r'change_lawyerProfile/(\d+)$', views.change_lawyerProfile, name='change_lawyerProfile'),

]
