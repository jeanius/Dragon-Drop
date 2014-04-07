from django.conf.urls import patterns, url
from dragondrop import views, user_views, ajax_views

urlpatterns = patterns('',
            url(r'^$', views.index, name='index'),
            url(r'^userpage[/]?$', views.userpage, name='userpage'),
            url(r'^userpage/(?P<query_in_url>\w+)$', views.userpageWithQuery, name='userpageWithQuery'),
            url(r'^bin-folder', views.binFolder, name='binFolder'),
            url(r'^register/$', user_views.register, name='register'),
            url(r'^ajax-drop-to-folder/$', ajax_views.ajaxDropToFolder, name='ajaxDropToFolder'),
            url(r'^ajax-change-bookmark-rank/$', ajax_views.ajaxChangeBookmarkRank, name='ajaxChangeBookmarkRank'),
            url(r'^ajax-drop-to-bin/$', ajax_views.ajaxDropToBin, name='ajaxDropToBin'),
            url(r'^ajax-create-folder/$', ajax_views.ajaxCreateFolder, name='ajaxCreateFolder'),
            url(r'^ajax-delete-bookmark/$', ajax_views.ajaxDeleteBookmark, name='ajaxDeleteBookmark'),
            url(r'^ajax-delete-folder/$', ajax_views.ajaxDeleteFolder, name='ajaxDeleteFolder'),
            url(r'^log_out/', views.log_out, name='log_out'),
            url(r'^privacy', views.privacy, name='privacy'),
            url(r'^help', views.help, name='help'),
            url(r'^about', views.about, name='about'),
            url(r'^goto', user_views.goto_url, name='goto'),
            url(r'^users/(?P<username>\w+)/$', user_views.user_folder_list, name='user_folder_list'),
            url(r'^users/(?P<username>\w+)/(?P<folder_page_url>\w+)/$', user_views.user_folder_view, name='user_folder_view'),
            url(r'^(?P<folder_page_url>\w+)/$', views.folder, name='folderpage'),


)
