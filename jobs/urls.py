from django.conf.urls import url
from .views import RecommendationsView, JobSearchView, ShortlistJobView
from django.conf import settings
from django.conf.urls.static import static


app_name = 'jobs'

urlpatterns = [
    url(r'^jobs/shortlist/(?P<pk>\d+)/$', ShortlistJobView.as_view(), name='shortlist'),
    url(r'^jobs/recommendations/$', RecommendationsView.as_view(), name='recommendations'),
    url(r'^jobs/search/(?P<param>[\w\- ]+)/(?P<value>[\w\- ]+)/$', JobSearchView.as_view(), name='search_job'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
