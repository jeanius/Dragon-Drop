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

def userpage(request):
     context = RequestContext(request)
  
     if request.user.is_authenticated():

        current_user = request.user
                 
        try:
            context_dict = {'bookmarklist': topten(request)}
            context_dict['user'] = current_user
            context_dict['folders'] = getFolderList(current_user, None)   
        except User.DoesNotExist:
               pass
     
        if request.method == 'POST':
            
            query = request.POST['query'].strip()
            if query:
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
                #print context_dict[]

        return render_to_response('userpage.html', context_dict, context)

     else:
         return render_to_response('index.html', {}, context)     

     
def register(request):
     context = RequestContext(request)
     
     registered = False
     username = None

     if request.method == 'POST':
          user_form = UserForm(data=request.POST)

          if user_form.is_valid():
               user = user_form.save()
               user.set_password(user.password)
               bin_folder = BinFolder.objects.create(busername_fk = user)
               user.save()
               username = request.POST['username']
               registered = True

          else:
               return render_to_response(
                      'register.html', {'registered': registered, 'user_form': user_form}, context)

     else:
          user_form = UserForm()

     return render_to_response(
               'register.html', {'registered': registered, 'username': username, 'user_form': user_form}, context)

def folder(request, folder_page_url):
    context = RequestContext(request)

    if request.user.is_authenticated():

        folder_name = decode_url(folder_page_url)
        context_dict = {'folder_name': folder_name}
        current_user = request.user
        context_dict['bookmarklist'] = topten(request)

        try:
            this_folder = current_user.folder_set.get(foldername = folder_name)
            context_dict['folders'] = getFolderList(current_user, folder_name, True)
            urlNotOk = False
            
            
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

            bf = this_folder.bookmarktofolder_set.all().order_by('-bfrank')
            def bf_to_bookmark(bf):
                bookmark = bf.bfbookmark
                bookmark.bfrank = bf.bfrank
                return bookmark
            context_dict['bookmarks'] = map(bf_to_bookmark, list(bf))

        except Folder.DoesNotExist:
            pass

        return render_to_response('folder.html', context_dict, context)

    else:
        return render_to_response('index.html')

def binFolder(request):
    context = RequestContext(request)

    if request.user.is_authenticated():
        context_dict = {'folder_name': "Bin Folder"}
        current_user = request.user
        bookmarklist = topten(request)
        context_dict['bookmarklist'] = bookmarklist
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

        drop_folder = request.user.folder_set.get(foldername = request.POST['folder_name'])
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
                                              
        message = "Link added" if added_to_folder else "Already there :)"
                              
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
    context = RequestContext(request)

    context_dict = bookmarksFoldersUsers(request)
   
    return render_to_response('help.html', context_dict, context) 

def privacy(request):
    context = RequestContext(request)
    
    context_dict = bookmarksFoldersUsers(request)
    
    return render_to_response('privacy.html', context_dict, context) 
    
def about(request):
    context = RequestContext(request)

    context_dict = {}
    context_dict = bookmarksFoldersUsers(request)
    
    return render_to_response('about.html', context_dict, context) 

def add_domain_to_search_result(search_result):
    search_result['domain'] = getDomain(search_result['link'])
    return search_result

# get relevant bookmarks and search results in sorted ranks order
def get_relevant_bookmarks_and_search_results(request, query, search_results):
    userBookmarks = Bookmark.objects.filter(fname__fusername_fk=request.user).distinct()
    relevantBookmarks = list(userBookmarks.filter( Q(url__icontains=query)    |
                                                  Q(bdescr__icontains=query) |
                                                  Q(btitle__icontains=query)))
    # make bookmarks that are in user bookmarks from the search results and append 
    # them - if necessary and not already in - to relevantBookmarks
    for search_result in search_results:
        if search_result['link'] in [b.url for b in relevantBookmarks]:
            search_results.remove(search_result)
        elif (search_result['link'] in [b.url for b in userBookmarks]) and (not search_result['link'] in relevantBookmarks):
            search_result['video_id'] = get_youtube_id(search_result['link'], search_result['domain'])
            relevantBookmarks.append(
                {'url': search_result['link'],
                'btitle': search_result['title'],
                'bdomain': search_result['domain'],
                'bdescr': search_result['summary'],
                'video_id': search_result['video_id']
                })
    # a list with the ranked relevant bookmarks
    ranks = list()
    # get the ranks if the relevant bookmarks and put them into the ranks list
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
            context_dict = {'bookmarklist': topten(request),
                            'user':         current_user,
                            'folders':      getFolderList(current_user, None)}
        except User.DoesNotExist:
               pass
        
    return context_dict

# get top ten saved bookmarks to display to users
def topten(request):
     topbookmark = Bookmark.objects.order_by('-saved_times')[:10]
     return topbookmark
