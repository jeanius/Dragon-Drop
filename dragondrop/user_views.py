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


def user_search_all(request, username):
    pass


def user_topic(request, username, folder_url):
    pass


