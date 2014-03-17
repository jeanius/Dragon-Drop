from django.conf.urls import patterns, url
from dragondrop import views

urlpatterns = patterns('',
            url(r'^$', views.index, name='index'),
            url(r'^userpage[/]?$', views.userpage, name='userpage'),
            url(r'^userpage/(?P<query_in_url>\w+)$', views.userpageWithQuery, name='userpageWithQuery'),
            url(r'^bin-folder', views.binFolder, name='binFolder'),
            url(r'^register/$', views.register, name='register'),
            url(r'^ajax-drop-to-folder/$', views.ajaxDropToFolder, name='ajaxDropToFolder'),
            url(r'^ajax-change-bookmark-rank/$', views.ajaxChangeBookmarkRank, name='ajaxChangeBookmarkRank'),
            url(r'^ajax-drop-to-bin/$', views.ajaxDropToBin, name='ajaxDropToBin'),
            url(r'^ajax-create-folder/$', views.ajaxCreateFolder, name='ajaxCreateFolder'),
            url(r'^ajax-delete-bookmark/$', views.ajaxDeleteBookmark, name='ajaxDeleteBookmark'),
            url(r'^ajax-delete-folder/$', views.ajaxDeleteFolder, name='ajaxDeleteFolder'),
            url(r'^log_out/', views.log_out, name='log_out'),
            url(r'^(?P<folder_page_url>\w+)/$', views.folder, name='folderpage'),
            url(r'^privacy', views.privacy, name='privacy'),
            url(r'^help', views.help, name='help'),
            url(r'^about', views.about, name='about'),
)
