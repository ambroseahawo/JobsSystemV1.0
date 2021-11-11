from django.conf.urls import url
from .views import AccountView, SignUpView, LoginView, LogoutView, AddExperienceView, AddInterestView, AddEducationView, \
    AddSkillView, DeleteExperienceView, DeleteInterestView, DeleteEducationView, DeleteSkillView, CompleteProfileView, \
    UploadDocumentsView, OpenMediaView, DeleteMediaView, RemoveShortlistedJobView
from django.conf import settings
from django.conf.urls.static import static

app_name = 'users'

urlpatterns = [
    url(r'^accounts/profile/jobs/shortlisted/(?P<pk>\d+)/remove', RemoveShortlistedJobView.as_view(), name='remove_shortlisted'),
    url(r'^accounts/profile/media/(?P<pk>\d+)/open', OpenMediaView.as_view(), name='open_media'),
    url(r'^accounts/profile/media/(?P<pk>\d+)/delete', DeleteMediaView.as_view(), name='del_media'),
    url(r'^accounts/profile/upload-documents/$', UploadDocumentsView.as_view(), name='upload_documents'),
    url(r'^accounts/profile/complete/$', CompleteProfileView.as_view(), name='complete_profile'),
    url(r'^accounts/profile/skills/(?P<pk>\d+)/delete/$', DeleteSkillView.as_view(), name='delete-skill'),
    url(r'^accounts/profile/education/(?P<pk>\d+)/delete/$', DeleteEducationView.as_view(), name='delete-education'),
    url(r'^accounts/profile/interests/(?P<pk>\d+)/delete/$', DeleteInterestView.as_view(), name='delete-interest'),
    url(r'^accounts/profile/experiences/(?P<pk>\d+)/delete/$', DeleteExperienceView.as_view(), name='delete-experience'),
    url(r'^accounts/profile/skills/add/$', AddSkillView.as_view(), name='add-skill'),
    url(r'^accounts/profile/education/add/$', AddEducationView.as_view(), name='add-education'),
    url(r'^accounts/profile/interests/add/$', AddInterestView.as_view(), name='add-interest'),
    url(r'^accounts/profile/experiences/add/$', AddExperienceView.as_view(), name='add-experience'),
    url(r'^accounts/login/$', LoginView.as_view(), name='login'),
    url(r'^accounts/logout/$', LogoutView.as_view(), name='logout'),
    url(r'^accounts/profile/$', AccountView.as_view(), name='account'),
    url(r'^accounts/signup/$', SignUpView.as_view(), name='sign-up')
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

