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
import simple_match

def index(request):
    context = RequestContext(request)

    if request.user.is_authenticated():
        return HttpResponseRedirect('userpage')

    else:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']

            user = authenticate(username=username, password=password)

            if user is not None:
                   login(request, user)
                   return HttpResponseRedirect('userpage')
            
            else:
                 return render_to_response('register.html', {'login_form': LoginForm}, context) #Return Register page if user not recognised
          
        else:
            return render_to_response('index.html', {'login_form': LoginForm}, context) 


def userpageWithQuery(request, query_in_url):
    request.query_in_url = query_in_url
    return userpage(request)


def userpage(request):
     context = RequestContext(request)
  
     if request.user.is_authenticated():

        current_user = request.user
                 
        try:
            context_dict = {'bookmarklist': topfive(request),
                            'latestfive'  : latestfive(request)}
            context_dict['user'] = current_user
            context_dict['folders'] = getFolderList(current_user, None)

        except User.DoesNotExist:
               pass
     
        query = False
        if request.method == 'POST':
            query = request.POST['query'].strip()
        elif hasattr(request, "query_in_url"):
            query = request.query_in_url.strip()
            
        if query:

            context_dict['suggested_folders'] = simple_match.search(query, request.user)

            # Run our Bing function to get the results list
            search_results = run_query(query)
            search_results = map(add_domain_to_search_result, search_results)
            # get relevant bookmarks and search results in sorted ranks order
            (relevantBookmarks, search_results) = get_relevant_bookmarks_and_search_results(request, query, search_results)
            
            for r in relevantBookmarks:
                containingFolders = [f.foldername for f in list(r.fname.filter(fusername_fk=request.user))]
                r.containingFolders = \
                    [{'name':f, 'underscored_name':encode_url(f)} for f in containingFolders]

            context_dict['search_results'] = search_results
            request.session['search_results'] = search_results
            context_dict['user_search_results'] = relevantBookmarks
            context_dict['search_query'] = query
            context_dict['search_query_urlencoded'] = encode_url(query)
            
            # Only show auto-created folder if a folder of the same name does not already exist
            context_dict['add_autocreated_folder'] = True
            for folder in context_dict['folders']:
                if folder.foldername.lower()==query.lower():
                    context_dict['add_autocreated_folder'] = False
        return render_to_response('userpage.html', context_dict, context)

     else:
         return render_to_response('index.html', {}, context)     

     
def folder(request, folder_page_url):
    context = RequestContext(request)

    if request.user.is_authenticated():

        folder_name = decode_url(folder_page_url)
        context_dict = {'folder_name': folder_name}
        current_user = request.user
        context_dict['bookmarklist'] = topfive(request)

        try:
            this_folder = current_user.folder_set.get(foldername = folder_name)
            context_dict['folders'] = getFolderList(current_user, folder_name, True)
            urlNotOk = False
            bookmarkWasAdded = False
            
            if request.method == 'POST':
                url = request.POST['url']

                try:
				    urllib.urlopen(url)
                except IOError:
					urlNotOk = True
					context_dict ['urlNotOk'] = urlNotOk
					   
                if not urlNotOk:
                    bookmark, bookmark_was_created = Bookmark.objects.get_or_create(url=url)
                    bookmark.saved_times += 1
                    if bookmark_was_created:   # If bookmark didn't already exist, set its properties
                        bookmark.btitle, bookmark.bdescr = getHtmlTitle(url)
                    maxRankInFolder = this_folder.bookmarktofolder_set.all().aggregate(Max('bfrank'))['bfrank__max']
                    bfrank = (maxRankInFolder or 0) + 1                 
                    bookmarkToFolder, added_to_folder = BookmarkToFolder.objects.get_or_create(
                                                  bffolder   = this_folder,
                                                  bfbookmark = bookmark)
                                              
                    bookmarkToFolder.bfrank = bfrank
                    bookmark.save()
                    bookmarkToFolder.save()
                    bookmarkWasAdded = True

            bf = this_folder.bookmarktofolder_set.all().order_by('-bfrank')
            
            def bf_to_bookmark(bf):
                bookmark = bf.bfbookmark
                bookmark.bfrank = bf.bfrank
                return bookmark
                
            bookmarksToDisplay = map(bf_to_bookmark, list(bf))
            if bookmarkWasAdded:
                bookmarksToDisplay[0].justAdded = True
            context_dict['bookmarks'] = bookmarksToDisplay

        except Folder.DoesNotExist:
            pass

        context_dict['latestfive'] = latestfive(request)
        return render_to_response('folder.html', context_dict, context)

    else:
        return render_to_response('index.html')

def binFolder(request):
    context = RequestContext(request)

    if request.user.is_authenticated():
        context_dict = {'folder_name': "Bin Folder"}
        current_user = request.user
        bookmarklist = topfive(request)
        context_dict['bookmarklist'] = bookmarklist
        context_dict['latestfive'] = latestfive(request)
        bin_folder = request.user.binfolder
        context_dict['folders'] = getFolderList(current_user, None)
        context_dict['bookmarks'] = bin_folder.bbmID_fk.all()
        context_dict['hideUrlInputBox'] = True
        return render_to_response('folder.html', context_dict, context)

    else:
        return render_to_response('index.html')

def getFolderList(current_user, current_folder_name, use_lighter_colour=False):
     try:
          folders = current_user.folder_set.all()
          for folder in folders:
              if folder.foldername == current_folder_name:
                  folder.url = None
                  folder.glyphicon_name = "glyphicon-folder-open"
                  if use_lighter_colour: folder.glyphicon_name += " keep-folder-open"
              else:
                  folder.glyphicon_name = "glyphicon-folder-close"
                  if use_lighter_colour: folder.glyphicon_name += " lighter-colour"
                  folder.url = encode_url(folder.foldername)
          return folders
     except User.DoesNotExist:
          return None

       
def encode_url(str):
    return str.replace(' ', '_')

def decode_url(str):
    return str.replace('_', ' ')

def log_out(request):
    context = RequestContext(request)
    if request.user.is_authenticated():
        logout(request)
        return render_to_response('index.html', {}, context)

def help(request):
    try:
        context = RequestContext(request)
        context_dict = bookmarksFoldersUsers(request)
        return render_to_response('help.html', context_dict, context) 
    except UnboundLocalError:
        return HttpResponseRedirect('userpage')

def privacy(request):
    try:
        context = RequestContext(request)
        context_dict = bookmarksFoldersUsers(request)
        return render_to_response('privacy.html', context_dict, context) 
    except UnboundLocalError:
        return HttpResponseRedirect('userpage')
    
def about(request):
    try:
        context = RequestContext(request)
        context_dict = {}
        context_dict = bookmarksFoldersUsers(request)
        return render_to_response('about.html', context_dict, context) 
    except UnboundLocalError:
        return HttpResponseRedirect('userpage')

def add_domain_to_search_result(search_result):
    search_result['domain'] = getDomain(search_result['link'])
    return search_result

# get relevant bookmarks and search results in sorted ranks order
def get_relevant_bookmarks_and_search_results(request, query, search_results):
    userBookmarks = Bookmark.objects.filter(fname__fusername_fk=request.user).distinct()
    relevantBookmarks = list(userBookmarks.filter(Q(url__icontains=query)    |
                                                  Q(bdescr__icontains=query) |
                                                  Q(btitle__icontains=query)))

    urlsOfRelevantBookmarks = [b.url for b in relevantBookmarks]
    urlsOfUserBookmarks = [b.url for b in userBookmarks]  # The URLs of all the current user's bookmarks
    
    # If any of out Bing search results are already in our list of relevant bookmarks,
    # then remove them from the list of Bing results
    search_results = [sr for sr in search_results if not sr['link'] in urlsOfRelevantBookmarks]
    
    # Get a list the all remaining Bing results that are already bookmarked
    already_bookmarked_results = [sr for sr in search_results if sr['link'] in urlsOfUserBookmarks]
    already_bookmarked_urls = [r['link'] for r in already_bookmarked_results]
    
    # From the Bing results, remove all remaining bookmarks
    search_results = [sr for sr in search_results if not sr['link'] in already_bookmarked_urls]
    
    # For each Bing search result that is bookmarked by that we didn't find
    # using simple text matching, add this bookmark to our (yellow) list of relevant bookmarks
    for url in already_bookmarked_urls:
        relevantBookmarks.append(userBookmarks.get(url=url))
    
    # Add YouTube IDs to search results
    for search_result in search_results:
        search_result['video_id'] = get_youtube_id(search_result['link'], search_result['domain'])

    # a list with the ranked relevant bookmarks
    ranks = list()
    # get the ranks of the relevant bookmarks and put them into the ranks list
    for r in relevantBookmarks:
        ranks.append(BookmarkToFolder.objects.filter(bffolder__fusername_fk = request.user, bfbookmark = r).values('bfrank')[0]['bfrank'])
    # sort the ranks list
    sorted(range(len(ranks)), reverse=True, key=lambda x:ranks[x])
    # sort the relevant bookmarks according to the sorted ranks
    try:
        relevantBookmarks = list(zip(*sorted(zip(ranks,relevantBookmarks)))[1])
        relevantBookmarks.reverse()
    except IndexError:
        relevantBookmarks = list()
    # remove bookmarks in bin from search results
    bin_urls = [b.url for b in request.user.binfolder.bbmID_fk.all()]
    search_results = [r for r in search_results if not r['link'] in bin_urls]
    return (relevantBookmarks, search_results)

def bookmarksFoldersUsers(request):
    context = RequestContext(request)

    if request.user.is_authenticated():
        current_user = request.user
        try:
            context_dict = {'bookmarklist': topfive(request),
                            'latestfive':   latestfive(request),
                            'user':         current_user,
                            'folders':      getFolderList(current_user, None)}
        except User.DoesNotExist:
               pass
        
    return context_dict

# get top ten saved bookmarks to display to users
def topfive(request):
     topbookmark = Bookmark.objects.order_by('-saved_times')[:5]
     return topbookmark
     
def latestfive(request):
    # Get latest 10 BookmarkToFolder objects
    latestBF = BookmarkToFolder.objects.filter(bffolder__fusername_fk=request.user).order_by('-datecreated')[:10]
    latestBookmarks = [bf.bfbookmark for bf in latestBF]
    latestBookmarks = list(OrderedDict.fromkeys(latestBookmarks)) # Get unique items
    return latestBookmarks[:5]
    
