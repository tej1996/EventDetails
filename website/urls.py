from django.conf.urls import url
from . import views

app_name = 'website'

urlpatterns = [
    url(r'^$', views.register, name='index'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^register/$', views.register, name='register'),
    url(r'^dashboard/$', views.dashboard, name='dashboard'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^new-event/$', views.new_event, name='new-event'),
]