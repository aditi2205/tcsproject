# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views import generic
from django.views.generic import TemplateView
from django.template import loader
from .models import Personaldetails, Responses,Result,Story
from django.views.generic.edit import CreateView
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.forms import  ModelForm
from rest_framework import generics, permissions
from rest_framework.response import Response
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.shortcuts import render_to_response
from formtools.wizard.views import SessionWizardView
from django.utils import timezone
from .decision import decision
#from .models import Result
#from django.contrib.formtools.wizard.views import SessionWizardView
from .forms import StoryForm
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
    print(form_list)
    print(form_dict)
    form_data=process_form_data(form_list)
    form0=form_dict['0'].save(commit=False);
    val=form_data[1]['q1']+form_data[1]['q2']+form_data[1]['q3']+form_data[1]['q4']+form_data[1]['q5']+ form_data[1]['q6'] + form_data[1]['q7'] + form_data[1]['q8'] + form_data[1]['q9'] + form_data[1]['q10'] +form_data[1]['q11'] + form_data[1]['q12'] + form_data[1]['q13'] + form_data[1]['q14'] + form_data[1]['q15']+ form_data[1]['q16'] + form_data[1]['q17'] + form_data[1]['q18'] + form_data[1]['q19'] + form_data[1]['q20'] + form_data[1]['q21']
    form0.Score=val
    
#THIS IS CODE FOR DIRECT ENTRY OF CLASS LABELS FOR TIME BEING 
#..DECISION TREE IS COMMENTED DONT DELETE COMMENTS

    if form0.Score <=10 & form0.Score >=1:
      form0.Resultp="These ups and downs are considered normal" 
    elif form0.Score <=16 & form0.Score >=11:
      form0.Resultp="Mild mood disturbance"
    elif form0.Score <=20 & form0.Score >=17:
       form0.Resultp="Borderline clinical depression"
    elif form0.Score <=30 & form0.Score >=21:
       form0.Resultp="Moderate depression" 
    elif form0.Score <=40 & form0.Score >=31:
       form0.Resultp= "Severe depression"
    else:
        form0.Resultp="Extreme depression" 

#CODE FOR DECISION TREE
    #data=list()
    #data.append(form0.Gender)
    #data.append(form0.RelationshipStatus)
    #data.append(form0.Occupation)
    #data.append(form0.Student)
    #data.append(form0.City)
    #data.append(form0.Age)
    #data.append(form0.Score)

    #response=decision(data)

    #form0.Resultp=response
    response=form0.Resultp
    form0.save()

    form1 = form_dict['1'].save(commit=False);
    form1.person=form0
    form1.result=val
    form1.save()

    # res=Result.create(result=val,Rid=form0).save();
    #response=decision.decision(form0)
    return render_to_response('portal/result.html',{'response':response})



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


def analysis1(request):
    return render(request, 'portal/analysis1.html')

def analysis2(request):
    male=int(Personaldetails.objects.filter(Gender='male').filter( Resultp = "high").count())
    female=int(Personaldetails.objects.filter(Gender='female').filter( Resultp = "high").count())
    return render(request, 'portal/analysis/analysis2.html',{'male':male,'female':female})

def analysis3(request):
    age1=int(Personaldetails.objects.filter( Age__lte ='10').filter(Age__gte = '0').filter( Resultp = "high").count())
    age2 = int(Personaldetails.objects.filter(Age__lte='20').filter(Age__gte = '10').filter( Resultp = "high").count())
    age3 = int(Personaldetails.objects.filter(Age__lte='30').filter(Age__gte = '20').filter( Resultp = "high").count())
    age4 = int(Personaldetails.objects.filter(Age__lte='40').filter(Age__gte = '30').filter( Resultp = "high").count())
    age5 = int(Personaldetails.objects.filter(Age__lte='50').filter(Age__gte = '50').filter(Resultp="high").count())
    age6 = int(Personaldetails.objects.filter(Age__gte='50').filter(Resultp="high").count())
    return render(request, 'portal/analysis/analysis3.html',{'age1':age1,'age2':age2, 'age3':age3, 'age4':age4, 'age5':age5, 'age6':age6})

def analysis4(request):
    s1=int(Personaldetails.objects.filter(Student__exact="School").filter(Resultp= "high").count())
    s2 = int(Personaldetails.objects.filter(Student__exact="College").filter(Resultp="high").count())

    return render(request, 'portal/analysis/analysis4.html',{'s1':s1,'s2':s2})

def analysis5(request):
    mm=int(Personaldetails.objects.filter(Resultp= "high").filter(RelationshipStatus = "Married").filter(Gender= "male").count())
    sm=int(Personaldetails.objects.filter(Resultp= "high").filter(RelationshipStatus = "Single").filter(Gender= "male").count())
    sf = int(Personaldetails.objects.filter(Resultp= "high").filter(RelationshipStatus = "Single").filter(Gender= "female").count())
    mf = int(Personaldetails.objects.filter(Resultp= "high").filter(RelationshipStatus = "Married").filter(Gender= "female").count())
    ml = int(Personaldetails.objects.filter(Resultp="high").filter(RelationshipStatus="live_in_relationship").filter(
        Gender="male").count())
    fl = int(Personaldetails.objects.filter(Resultp="high").filter(RelationshipStatus="live_in_relationship").filter(
        Gender="female").count())
    mf = int(Personaldetails.objects.filter(Resultp="high").filter(RelationshipStatus="fling").filter(
        Gender="male").count())
    ff = int(Personaldetails.objects.filter(Resultp="high").filter(RelationshipStatus="fling").filter(
        Gender="female").count())
    #querym='''SELECT Gender FROM portal_personaldetails WHERE Gender='male' AND Pid IN (SELECT id FROM portal_responses WHERE q1=2)'''
    #queryf='''SELECT Gender FROM portal_personaldetails WHERE Gender='female' AND Pid IN (SELECT id FROM portal_responses WHERE q1=2)'''
    return render(request, 'portal/analysis/analysis5.html',{'mm':mm, 'mf': mf, 'sm': sm, 'sf': sf, 'ml': ml, 'fl': fl, 'mf': mf, 'ff': ff})

def analysis6(request):
    tp=int(Personaldetails.objects.filter(Resultp= "high").filter(Occupation = "Professional").count())
    tb=int(Personaldetails.objects.filter(Resultp= "high").filter(Occupation = "Business").count())
    fp = int(Personaldetails.objects.filter(Resultp= "high").filter(Occupation = "Professional").filter(Gender= "female").count())
    mp = int(Personaldetails.objects.filter(Resultp= "high").filter(Occupation = "Professional").filter(Gender= "male").count())
    mb = int(Personaldetails.objects.filter(Resultp="high").filter(Occupation = "Business").filter(
        Gender="male").count())
    fb = int(Personaldetails.objects.filter(Resultp="high").filter(Occupation = "Business").filter(
        Gender="female").count())


    return render(request, 'portal/analysis/analysis6.html',{'tp':tp, 'tb': tb, 'fp': fp, 'mp': mp, 'fp': fp, 'mb': mb, 'fb': fb})


def stories(request):
    stories = Story.objects.filter(time__lte=timezone.now()).order_by('-time')
    return render(request, 'portal/stories.html', {'stories':stories})

def story_new(request):
    if request.method == "POST":
        form = StoryForm(request.POST)
        if form.is_valid():
            story = form.save(commit=False)
            story.time = timezone.now()
            story.save()
            return redirect('stories')
    else:
        form = StoryForm()
    return render(request, 'portal/new_story.html', {'form': form})
