from django.conf.urls import patterns, url
from dragondrop import views

urlpatterns = patterns('',
            url(r'^$', views.index, name='index'),
            url(r'userpage', views.userpage, name='userpage'),
)
