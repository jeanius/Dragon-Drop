from django.conf.urls import patterns, url
from dragondrop import views

urlpatterns = patterns('',
            url(r'^$', views.index, name='index'),
            url(r'^userpage/(?P<user_page_url>\w+)/$', views.userpage, name='userpage'),
            url(r'^register/$', views.register, name='register'),
)
