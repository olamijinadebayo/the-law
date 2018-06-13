from django.conf.urls import url, include
from .import views 

app_name='lawyer'

urlpatterns = [
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^$', views.lawyerdashboard, name= 'lawyerdashboard'),
    url(r'profile/', views.lawyerprofile, name = 'lawyerprofile'),
    url(r'cases/', views.lawyercases, name = 'lawyercases'),
    url(r'new/article', views.newarticle, name = 'newarticle'),
    url(r'change_lawyerProfile/(\d+)$', views.change_lawyerProfile, name='change_lawyerProfile'),
    url(r'^logout/$', views.logout_view, name='logout')
]
