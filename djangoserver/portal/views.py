# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views import generic
from django.views.generic import TemplateView
from django.template import loader
from .models import Personaldetails, Responses, Result
from django.views.generic.edit import CreateView
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.forms import ModelForm
# Create your views here.
def home(request):
	template=loader.get_template('portal/index.html')
	context=None
	return HttpResponse(template.render(context,request))
   # return HttpResponse("Hello, world. You're at the portal Quiz.")
   
class FillInfo(CreateView):
 model= Personaldetails
 fields=['Pid','Name','Gender','RelationshipStatus','Occupation','Student','City','Age','Email_id']
 success_url = reverse_lazy('quiz')

#def quiz(request):
    #template=loader.get_template('portal/info.html')
	#context=None
	#return HttpResponse(template.render(context,request))

class letsplay(CreateView):
    model= Responses
    fields=['q1','q2','q3','q4','q5']
    success_url = ('quizres')



def quizres(request):
    template= loader.get_template('portal/quizres.html')


def quiz(request):
    template = loader.get_template('portal/quiz.html')
    context = None
    return HttpResponse(template.render(context, request))



def analysis(request):
    return HttpResponse("Hello, world. You're at the portal analysis.")
    
def forum(request):
    return HttpResponse("Hello, world. You're at the portal forum.")