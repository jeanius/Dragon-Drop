from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response
from dragondrop.forms import UserForm, LoginForm
from django.contrib.auth.models import User
from django.db.models import Q
from dragondrop.bing_search import run_query
from dragondrop.models import Folder, Bookmark, BookmarkToFolder
from dragondrop.get_domain_from_url import getDomain
from dragondrop.get_web_page_title import getHtmlTitle
from django.contrib.auth import authenticate, login, logout

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
                 return render_to_response('index.html', {'login_form': LoginForm}, context)
          
        else:
            return render_to_response('index.html', {'login_form': LoginForm}, context) 

def userpage(request):
     context = RequestContext(request)
  
     if request.user.is_authenticated():

        current_user = request.user
                 
        try:
            bookmarklist = topten(request)  
            context_dict = {'bookmarklist': bookmarklist}
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
                   context_dict['search_results'] = search_results
                   request.session['search_results'] = search_results

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
          bookmarklist = topten(request)  
          context_dict = {'bookmarklist': bookmarklist}

          try:
             this_folder = Folder.objects.filter(foldername = folder_name)   \
                                            .filter(fusername_fk=current_user)[0]
             context_dict['folders'] = getFolderList(current_user, folder_name, True)
             bookmarks = Bookmark.objects.filter(fname = this_folder)
             context_dict['bookmarks'] = bookmarks
             
             if request.method == 'POST':
                 url = request.POST['url']
                 bookmark, bookmark_was_created = Bookmark.objects.get_or_create(url=url)  
                 bookmark.saved_times += 1
                 if bookmark_was_created:   # If bookmark didn't already exist, set its properties
                     bookmark.btitle, bookmark.bdescr = getHtmlTitle(url)
                     bookmarkToFolder = BookmarkToFolder.objects.create(
                                              bffolder   = this_folder,
                                              bfbookmark = bookmark)
                     bookmark.save()
                     bookmarkToFolder.save()
                 else:
                     bookmark.save()
                 

          except Folder.DoesNotExist:
             pass

          return render_to_response('folder.html', context_dict, context)

     else:
          return render_to_response('index.html')

def getFolderList(current_user, current_folder_name, use_lighter_colour=False):
     try:
          folders = Folder.objects.filter(fusername_fk=current_user)
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


# This is a work in progress - when a search-result bookmark is dragged onto
# a folder, it should add the link to the folder.
def ajaxDropToFolder(request):
    if request.method == 'POST':
        url = request.POST['url']
        bookmark, bookmark_was_created = Bookmark.objects.get_or_create(url=url)

        bookmark.saved_times += 1

        if bookmark_was_created:    # If bookmark didn't already exist, set its properties
            search_result_for_this_url = filter(lambda x: x['link'] == url,
                                                request.session['search_results'])[0]
            bookmark.btitle = search_result_for_this_url['title']
            bookmark.bdescr = search_result_for_this_url['summary']

        drop_folder = Folder.objects.filter(foldername = request.POST['folder_name'])   \
                                      .filter(fusername_fk=request.user)[0]
        bookmarkToFolder, _ = BookmarkToFolder.objects.get_or_create(
                                          bffolder   = drop_folder,
                                          bfbookmark = bookmark)                         
        bookmark.save()
        bookmarkToFolder.save()

        return HttpResponse('success adding ' + request.POST['url'] + ' to folder')

def encode_url(str):
    return str.replace(' ', '_')

def decode_url(str):
    return str.replace('_', ' ')

def topten(request):
     topbookmark = Bookmark.objects.order_by('-saved_times')[:10]
     return topbookmark

def log_out(request):
    context = RequestContext(request)
    if request.user.is_authenticated():
        logout(request)
        print "Hello"
        return render_to_response('index.html', {}, context)

def help(request):
    return render_to_response('help.html') 

def privacy(request):
    return render_to_response('privacy.html') 
    
def about(request):
    return render_to_response('about.html') 


def add_domain_to_search_result(search_result):
    search_result['domain'] = getDomain(search_result['link'])
    return search_result

