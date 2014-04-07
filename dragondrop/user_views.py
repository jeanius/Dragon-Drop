from dragondrop.views import decode_url, encode_url, topfive, getFolderList, latestfive

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
from django.shortcuts import redirect

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
               password = request.POST['password']
               user = authenticate(username=username, password=password)
               login(request, user)
               return HttpResponseRedirect('/userpage')

          else:
               return render_to_response(
                      'register.html', {'registered': registered, 'user_form': user_form}, context)

     else:
          user_form = UserForm()

     return render_to_response(
               'register.html', {'registered': registered, 'username': username, 'user_form': user_form}, context)


def goto_url(request):
    context = RequestContext(request)
    bm_id = None
    url = '/'
    if request.method == 'GET':
        if 'bm_id' in request.GET:
            bm_id = request.GET['bm_id']
            try:
                bm = Bookmark.objects.get(id=bm_id)
                bm.clicks = bm.clicks + 1
                bm.save()
                url = bm.url
            except:
                pass

    return redirect(url)



def user_folder_view(request, username, folder_page_url):
    context = RequestContext(request)

    if request.user.is_authenticated():

        folder_name = decode_url(folder_page_url)
        context_dict = {'folder_name': folder_name,
                        'folder_username': username,
                        'folder_username_encoded': encode_url(username)}
        current_user = request.user
        folder_owner = User.objects.get(username=username)
        context_dict['bookmarklist'] = topfive(request)

        try:
            this_folder = folder_owner.folder_set.get(foldername = folder_name)
            context_dict['folders'] = getFolderList(current_user, folder_name, True)

            bf = this_folder.bookmarktofolder_set.all().order_by('-bfrank')
            
            def bf_to_bookmark(bf):
                bookmark = bf.bfbookmark
                bookmark.bfrank = bf.bfrank
                return bookmark
                
            context_dict['bookmarks'] = map(bf_to_bookmark, list(bf))

        except Folder.DoesNotExist:
            pass

        context_dict['latestfive'] = latestfive(request)
        return render_to_response('public-folder-temporary.html', context_dict, context)

    else:
        return render_to_response('index.html')





def user_folder_list(request, username):
    context = RequestContext(request)

    if request.user.is_authenticated():

        current_user = request.user
        folder_owner = User.objects.get(username=username)
        context_dict = {
                         'bookmarklist': topfive(request),
                         'username': username,
                         'username_encoded': encode_url(username)
                       }
        
        folder_list = getFolderList(folder_owner, None)
        folder_list = [{"name":f.foldername, "url_encoded_name":encode_url(f.foldername)} for f in folder_list]
        context_dict['public_folder_list'] = folder_list

        context_dict['latestfive'] = latestfive(request)
        return render_to_response('public-folder-list.html', context_dict, context)

    else:
        return render_to_response('index.html')

