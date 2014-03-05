from django.conf.urls import patterns, url
from dragondrop import views

urlpatterns = patterns('',
            url(r'^$', views.index, name='index'),
            url(r'^userpage/', views.userpage, name='userpage'),
            url(r'^register/$', views.register, name='register'),
            url(r'^ajax-drop-to-folder/$', views.ajaxDropToFolder, name='ajaxDropToFolder'),
            url(r'^/(?P<folder_page_url>\w+)/$', views.folder, name='folderpage'),
)
