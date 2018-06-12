from django.conf.urls import url
from . import views

# namespace url
app_name = 'lawyer'


urlpatterns = [
    url(r'^signup/$', views.signup, name='signup')
]
