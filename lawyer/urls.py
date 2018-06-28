from django.conf.urls import url, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
app_name = 'lawyer'

urlpatterns = [
    url(r'^$', views.lawyerdashboard, name='lawyerdashboard'),
    url(r'^profile/(\d+)/$', views.profile, name='lawyerprofile'),
    url(r'^edit/', views.edit_profile, name='edit'),
    url(r'cases/', views.lawyercases, name='lawyercases'),
    url(r'new/article', views.newarticle, name='newarticle'),
    url(r'^lawyer_form', views.lawyer_form, name='lawyer_form'),
    url(r'^portal', views.portal, name='portal'),
    url(r'^data$', views.reported, name='lawyers'),
    url(r'^google$', views.google, name='google'),
    url(r'article', views.lawyerarticles, name='articles'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
