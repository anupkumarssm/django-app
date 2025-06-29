from django.shortcuts import render
# app/views.py
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def home(request):
    return HttpResponse("Hello Anup -- How are you... ? ")

def homepage(request):
  template = loader.get_template('home.html')
  return HttpResponse(template.render())