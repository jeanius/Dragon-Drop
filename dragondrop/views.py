from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from dragondrop.forms import UserForm
from django.contrib.auth.models import User

def index(request):
     context = RequestContext(request)
     return render_to_response('index.html')

def userpage(request, user_page_url):
     context = RequestContext(request)
     
     user_name = user_page_url.replace('_', ' ')

     context_dict = {'user_name': user_name}

     try:
          users = User.objects.get(username=user_name)
          context_dict['user'] = users

     except User.DoesNotExist:
          pass
     
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


