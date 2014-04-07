import dragondrop.views

# I just copied the imports from views.py. There are some unused ones here! -JT
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response
from dragondrop.forms import UserForm, LoginForm
from django.contrib.auth.models import User
from django.db.models import Q, Max
from dragondrop.bing_search import run_query
from dragondrop.models import Folder, Bookmark, BookmarkToFolder, BinFolder
from dragondrop.get_domain_from_url import getDomain
from dragondrop.get_web_page_title import getHtmlTitle
from django.contrib.auth import authenticate, login, logout
from dragondrop.url_utilities import get_youtube_id
from urlparse import urlparse
from operator import itemgetter
import urllib
import bisect
from collections import OrderedDict


# When a search-result bookmark is dragged onto
# a folder, it should add the link to the folder.
def ajaxDropToFolder(request):
    if request.method == 'POST' and request.user.is_authenticated():
        url = request.POST['url']
        bookmark, bookmark_was_created = Bookmark.objects.get_or_create(url=url)
        print "created??? " + str(bookmark_was_created)
        bookmark.saved_times += 1

        if bookmark_was_created:    # If bookmark didn't already exist, set its properties
            search_result_for_this_url = filter(lambda x: x['link'] == url,
                                                request.session['search_results'])[0]
            bookmark.btitle = search_result_for_this_url['title']
            bookmark.bdescr = search_result_for_this_url['summary']

        drop_folder, folder_was_created = request.user.folder_set.get_or_create(foldername = request.POST['folder_name'])
        bookmark_to_folder_set = drop_folder.bookmarktofolder_set.all()
        if bookmark_to_folder_set.count() > 0:
            bfrank = bookmark_to_folder_set.aggregate(Max('bfrank'))['bfrank__max'] + 1
        else:
            bfrank = 0
        bookmarkToFolder, added_to_folder = BookmarkToFolder.objects.get_or_create(
                                              bffolder   = drop_folder,
                                              bfbookmark = bookmark)   
        bookmarkToFolder.bfrank = bfrank
        try:
            bin_folder = request.user.binfolder
            bin_folder.bbmID_fk.remove(bookmark)
        except BinFolder.DoesNotExist:
            pass
                
        if folder_was_created:
            message = "Folder created and link added"        
        elif added_to_folder:       
            message = "Link added"
        else:
            message = "Already there :)"
                              
        bookmark.save()
        bookmarkToFolder.save()

        return HttpResponse(message)

def ajaxChangeBookmarkRank(request):
    if request.method == 'POST' and request.user.is_authenticated():
        bookmark = Bookmark.objects.get(url=request.POST['url'])
        this_folder = request.user.folder_set.get(foldername = request.POST['folder_name'])
        try:
            bookmarkToFolder = BookmarkToFolder.objects.get(bffolder   = this_folder,
                                                            bfbookmark = bookmark)                              
            bookmarkToFolder.bfrank = request.POST['new_rank']
            bookmarkToFolder.save()
            return HttpResponse("Rank changed")
        except Bookmark.DoesNotExist:
            return HttpResponse("The bookmark is not in this folder")
 
def ajaxDropToBin(request):
    if request.method == 'POST' and request.user.is_authenticated():
        url = request.POST['url']
        bookmark, bookmark_was_created = Bookmark.objects.get_or_create(url=url)

        bookmark.saved_times += 1

        if bookmark_was_created:    # If bookmark didn't already exist, set its properties
            search_result_for_this_url = filter(lambda x: x['link'] == url,
                                                request.session['search_results'])[0]
            bookmark.btitle = search_result_for_this_url['title']
            bookmark.bdescr = search_result_for_this_url['summary']
            
        bin_folder, _ = BinFolder.objects.get_or_create(busername_fk = request.user)
        bin_folder.bbmID_fk.add(bookmark)
 
        bookmarkToFolder = BookmarkToFolder.objects.filter(
                                              bffolder__fusername_fk = request.user,
                                              bfbookmark = bookmark)
        bookmarkToFolder.delete()
                                              
        message = "Link added"
                              
        bookmark.save()

        return HttpResponse(message)

def ajaxDeleteBookmark(request):
    if request.method == 'POST' and request.user.is_authenticated():
        url = request.POST['bookmarkUrl']
        bookmark = Bookmark.objects.get(url=url)
        foldername = request.POST['folderName']
        if foldername == 'Bin Folder':
            bin_folder = request.user.binfolder
            bin_folder.bbmID_fk.remove(bookmark)
        else:
            bookmark.saved_times -= 1
            this_folder = request.user.folder_set.get(foldername = request.POST['folderName'])
            bookmarkToFolder = BookmarkToFolder.objects.get(
                                              bffolder   = this_folder,
                                              bfbookmark = bookmark)             
            bookmarkToFolder.delete()
        return HttpResponse("Bookmark deleted")
        
def ajaxCreateFolder(request):
    if request.method == 'POST' and request.user.is_authenticated():
        folderName = request.POST['folderName']
        if folderName == "":
            return HttpResponse("Enter a folder name")
        if folderName.lower() in ["about", "privacy", "help", "log_out", "userpage", "register"]:
            return HttpResponse("Sorry, that name isn't available.")
        if folderName == "bin-folder" or folderName == "bin_folder" or folderName == "bin folder":
            return HttpResponse("You already have a bin folder!")		
        folder, folder_was_created = Folder.objects.get_or_create(foldername=folderName, fusername_fk=request.user)
        if folder_was_created:
            return HttpResponse("Folder created")
        else:
            return HttpResponse("Folder already exists")
        
def ajaxDeleteFolder(request):
    if request.method == 'POST' and request.user.is_authenticated():
        folderName = request.POST['folderName']
        folder = Folder.objects.get(foldername=folderName, fusername_fk=request.user)
        BookmarkToFolder.objects.filter(bffolder = folder).delete()
        folder.delete()
        return HttpResponse("Folder deleted")
