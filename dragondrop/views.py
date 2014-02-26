from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response

def index(request):
     context = RequestContext(request)
     return render_to_response('templates\index.html')

def userpage(request):
     context = RequestContext(request)
     return render_to_response('templates\userpage.html')
