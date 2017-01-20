from django.conf.urls import url
from django.contrib import auth

from . import views
from django.contrib.auth.views import (
    password_change,
    password_change_done,
)
app_name = 'website'


urlpatterns = [
    url(r'^$', views.register, name='index'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^register/$', views.register, name='register'),
    url(r'^dashboard/$', views.dashboard, name='dashboard'),
    url(r'^profile/$', views.user_profile, name='profile'),
    url(r'^new-event/$', views.new_event, name='new-event'),
    url(r'^delete-event/(?P<eventid>\d+)$', views.delete_event, name='delete-event'),
    url(r'^allow/(?P<eid>\d+)/$', views.allow, name='allow'),
    url(r'^entries/(?P<eventid>\d+)/$', views.entries, name='entries'),
    url(r'^edit-event/(?P<eventid>\d+)/$', views.edit_event, name='edit-event'),
    url(r'^event-info/(?P<eventid>\d+)/$', views.event_info, name='event-info'),
    url(r'^download/(?P<eventid>\d+)/$', views.download, name='download'),
    url(r'^password/$', views.change_password, name='change_password'),
]
