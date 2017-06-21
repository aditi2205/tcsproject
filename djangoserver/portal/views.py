# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views import generic
from django.views.generic import TemplateView
from django.template import loader
from .models import Personaldetails, Responses,Result
from django.views.generic.edit import CreateView
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.forms import  ModelForm
from rest_framework import generics, permissions
from rest_framework.response import Response
from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import render_to_response
from formtools.wizard.views import SessionWizardView
#from .models import Result
#from django.contrib.formtools.wizard.views import SessionWizardView
from .forms import DetailsForm,Quiz
# Create your views here.
def home(request):
	template=loader.get_template('portal/index.html')
	context=None
	return HttpResponse(template.render(context,request))
   # return HttpResponse("Hello, world. You're at the portal Quiz.")
   
#def FillInfo(request):
class ContactWizard(SessionWizardView):
  template_name="portal/wizard_quiz.html"
  def done(self, form_list,form_dict,**kwargs):
        form_data=process_form_data(form_list)
        form0 = form_dict['0'].save();
        form1 = form_dict['1'].save();
        val=form_data[1]['q1']+form_data[1]['q2']+form_data[1]['q3']+form_data[1]['q4']+form_data[1]['q5']
        res=Result(result=val).save();
        


        return render_to_response('portal/result.html',{'val':val})



def process_form_data(form_list):
  form_data= [form.cleaned_data for form in form_list]
  return form_data
  #return form_data;


    #if request.method == 'POST':

     # form = DetailsForm(request.POST)
     # form2 = Quiz(request.POST)
     # if form.is_valid() and form2.is_valid():
     #   details = form.save()
      #  quiz = form.save()
        
        #if request.method == 'POST':

          #form2 = Quiz(request.POST)
          #if form2.is_valid():
            #quiz = form.save()
        
            #return HttpResponse('Quiz done')
        
          #else:
           # return HttpResponse('Quiz done not')

       # else:
       #  form2 = Quiz()
        #  return render(request,'portal/quiz_form.html', { 'form2': form2})




        
      #  return HttpResponse('done both')
      #else:
      #  return HttpResponse('done not')

    #else:
    #    form = DetailsForm()
     #   form2 = Quiz()
     #   return render(request,'portal/details_form.html', { 'form': form,'form2':form2 })
        

 
    #success_url = reverse_lazy('quiz')

#def quiz(request):
    #template=loader.get_template('portal/info.html')
	#context=None
	#return HttpResponse(template.render(context,request))


  #def letsplay(request):
    #if request.method == 'POST':

     # form = Quiz(request.POST)
      #if form.is_valid():
      #  quiz = form.save()
        
       # return HttpResponse('done')
        #return redirect('post_detail', pk=post.pk)
     # else:
     #   return HttpResponse('done not')

    #else:
       # form = Quiz()
       # return render(request,'portal/quiz_form.html', { 'form': form})


#def quizres(request):
  # template= loader.get_template('portal/quizres.html')


#def quizres(request):
  #  template = loader.get_template('portal/quiz.html')
  #  context = None
  #  return HttpResponse(template.render(context, request))



def analysis(request):
    return HttpResponse("Hello, world. You're at the portal analysis.")
    
def forum(request):
    return HttpResponse("Hello, world. You're at the portal forum.")