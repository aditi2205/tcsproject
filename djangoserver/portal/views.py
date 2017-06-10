# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import TemplateView
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def home(request):
	template=loader.get_template('portal/index.html')
	context=None
	return HttpResponse(template.render(context,request))
   # return HttpResponse("Hello, world. You're at the portal Quiz.")
    

def quiz(request):
    return HttpResponse("Hello, world. You're at the portal Quiz.")
    
def analysis(request):
    return HttpResponse("Hello, world. You're at the portal analysis.")
    
def forum(request):
    return HttpResponse("Hello, world. You're at the portal forum.")