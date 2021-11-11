from django.conf.urls import url
from .views import IndexView
from django.conf import settings
from django.conf.urls.static import static


app_name = 'home'

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index')
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
