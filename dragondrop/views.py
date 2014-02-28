from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from dragondrop.forms import UserForm
from django.contrib.auth.models import User
from dragondrop.bing_search import run_query


def index(request):
     context = RequestContext(request)
     return render_to_response('index.html')

def userpage(request, user_page_url):
     context = RequestContext(request)
     
     user_name = decode_url(user_page_url)
     context_dict = {'user_name': user_name}

     try:
          users = User.objects.get(username=user_name)
          context_dict['user'] = users
          folders = Folder.objects.filter(fusername_fk=users)
          context_dict['folders'] = folders
          for folder in folders:
               folder.url = encode_url(folder.foldername)
          
     except User.DoesNotExist:
          pass
   
     if request.method == 'POST':
        query = request.POST['query'].strip()
        if query:
          # Run our Bing function to get the results list
          context_dict['search_results'] = run_query(query)
     
     return render_to_response('userpage.html', context_dict, context)

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
               formerrors =  user_form.errors
               return render_to_response(
                      'register.html', {'registered': registered, 'user_form': user_form}, context)

     else:
          user_form = UserForm()

     return render_to_response(
               'register.html', {'registered': registered, 'username': username, 'user_form': user_form}, context)

def folder(request, folder_name_url):
     context = RequestContext(request)

     folder_name = decode_url(folder_page_url)
     context_dict = {'folder_name': folder_name}

     try:
          folders = Folder.objects.filter(foldername = folder_name)
          context_dict['folders'] = folders
          bookmarks = Bookmark.objects.filter(fname = folders)
          context_dict['bookmarks'] = bookmarks

     except Folder.DoesNotExist:
          pass

     return render_to_response('folder.html', context_dict, context)

     
def encode_url(str):
    return str.replace(' ', '_')

def decode_url(str):
    return str.replace('_', ' ')

