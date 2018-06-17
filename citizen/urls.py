from django.conf.urls import url
# from django.conf import settings
# from django.conf.urls.static import static
from . import views
import lawyer

app_name = 'citizen'

urlpatterns = [
    url(r'^home/$', views.home, name='home'),
    url(r'^advocates/$', views.advocates, name='advocates'),
    url(r'^post/$', views.post, name='post'),
    url(r'^profile/', views.profile_edit, name='edit'),
]
# if settings.DEBUG:
#     urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)