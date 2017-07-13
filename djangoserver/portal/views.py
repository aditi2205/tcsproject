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
from django.db.models import Q
from .decision import decision
#from .models import Result
#from django.contrib.formtools.wizard.views import SessionWizardView
from .forms import StoryForm,CommentForm
from .forms import DetailsForm,Quiz
from textblob import TextBlob
from .sentiment import sentiment
# Create your views here.
def home(request):
    template=loader.get_template('portal/index.html')
    context=None
    return HttpResponse(template.render(context,request))
   # return HttpResponse("Hello, world. You're at the portal Quiz.")
def result(request):
    return render(request, 'portal/result.html')

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

    if form0.Score <=10 and form0.Score >=0:
      form0.Resultp="These ups and downs are considered normal"
    elif form0.Score <=16 and form0.Score >=11:
      form0.Resultp="Mild mood disturbance"
    elif form0.Score <=20 and form0.Score >=17:
       form0.Resultp="Borderline clinical depression"
    elif form0.Score <=30 and form0.Score >=21:
       form0.Resultp="Moderate depression"
    elif form0.Score <=40 and form0.Score >=31:
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
    return render_to_response('portal/result.html',{'response':response, 'Score':form0.Score})



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

def analysis0(request):
    s1=int(Personaldetails.objects.filter(Resultp__exact= "These ups and downs are considered normal").count())
    s3 = int(Personaldetails.objects.filter(Resultp__exact= "Mild mood disturbance").count())
    s4 = int(Personaldetails.objects.filter(Resultp__exact= "Borderline clinical depression").count())
    s5 = int(Personaldetails.objects.filter(Resultp__exact= "Moderate depression").count())
    s6 = int(Personaldetails.objects.filter(Resultp__exact="Severe depression").count())
    s7 = int(Personaldetails.objects.filter(Resultp__exact="Extreme depression").count())

    return render(request, 'portal/analysis/analysis0.html',{'s1':s1,'s3':s3,'s4':s4, 's5':s5,'s6':s6, 's7':s7})


def analysis2(request):
    male=int(Personaldetails.objects.filter(Gender='male').filter(Q(Resultp= "Moderate depression")|Q(Resultp= "Extreme depression")| Q(Resultp= "Severe depression")).count())
    female=int(Personaldetails.objects.filter(Gender='female').filter(Q(Resultp= "Moderate depression")|Q(Resultp= "Extreme depression")| Q(Resultp= "Severe depression")).count())
    return render(request, 'portal/analysis/analysis2.html',{'male':male,'female':female})

def analysis3(request):
    agea=int(Personaldetails.objects.filter( Age__lte ='10').filter(Age__gte = '0').filter( Resultp = "Severe depression").count())
    ageb = int(
        Personaldetails.objects.filter(Age__lte='10').filter(Age__gte='0').filter(Resultp="Extreme depression").count())
    age1= agea+ageb
    agec = int(Personaldetails.objects.filter(Age__lte='20').filter(Age__gte = '10').filter( Resultp = "Severe depression").count())
    aged = int(
        Personaldetails.objects.filter(Age__lte='20').filter(Age__gte='10').filter(Resultp="Extreme depression").count())
    age2= agec+aged
    agee = int(Personaldetails.objects.filter(Age__lte='30').filter(Age__gte = '20').filter( Resultp = "Severe depression").count())
    agef = int(
        Personaldetails.objects.filter(Age__lte='30').filter(Age__gte='20').filter(Resultp="Extreme depression").count())
    age3= agee+agef
    ageg = int(Personaldetails.objects.filter(Age__lte='40').filter(Age__gte = '30').filter( Resultp = "Severe depression").count())
    ageh = int(
        Personaldetails.objects.filter(Age__lte='40').filter(Age__gte='30').filter(Resultp="Extreme depression").count())
    age4= ageg+ageh
    agei = int(Personaldetails.objects.filter(Age__lte='50').filter(Age__gte = '50').filter(Resultp="Severe depression").count())
    agej = int(Personaldetails.objects.filter(Age__lte='50').filter(Age__gte='50').filter(
        Resultp="Extreme depression").count())
    age5= agei+agej;

    agek = int(Personaldetails.objects.filter(Age__gte='50').filter(Resultp="Severe depression").count())
    agel = int(Personaldetails.objects.filter(Age__gte='50').filter(Resultp="Extreme depression").count())
    age6= agek+ agel
    return render(request, 'portal/analysis/analysis3.html',{'age1':age1,'age2':age2, 'age3':age3, 'age4':age4, 'age5':age5, 'age6':age6})

def analysis4(request):
    sa=int(Personaldetails.objects.filter(Student__exact="School").filter(Resultp= "Severe depression").count())
    sb=int(Personaldetails.objects.filter(Student__exact="School").filter(Resultp= "Extreme depression").count())
    s1= sa+sb
    sc= int(Personaldetails.objects.filter(Student__exact="College").filter(Resultp="Severe depression").count())
    sd=int(Personaldetails.objects.filter(Student__exact="College").filter(Resultp="Extreme depression").count())
    s2 = sc+sd

    return render(request, 'portal/analysis/analysis4.html',{'s1':s1,'s2':s2})

def analysis5(request):
    mm=int(Personaldetails.objects.filter(Q(Resultp= "Extreme depression")| Q(Resultp= "Severe depression")).filter(RelationshipStatus = "Married").filter(Gender= "male").count())
    sm=int(Personaldetails.objects.filter(Q(Resultp= "Extreme depression")| Q(Resultp= "Severe depression")).filter(RelationshipStatus = "Single").filter(Gender= "male").count())
    sf = int(Personaldetails.objects.filter(Q(Resultp= "Extreme depression")| Q(Resultp= "Severe depression")).filter(RelationshipStatus = "Single").filter(Gender= "female").count())
    mf = int(Personaldetails.objects.filter(Q(Resultp= "Extreme depression")| Q(Resultp= "Severe depression")).filter(RelationshipStatus = "Married").filter(Gender= "female").count())
    ml = int(Personaldetails.objects.filter(Q(Resultp= "Extreme depression")| Q(Resultp= "Severe depression")).filter(RelationshipStatus="live_in_relationship").filter(
        Gender="male").count())
    fl = int(Personaldetails.objects.filter(Q(Resultp= "Extreme depression")| Q(Resultp= "Severe depression")).filter(RelationshipStatus="live_in_relationship").filter(
        Gender="female").count())
    mf = int(Personaldetails.objects.filter(Q(Resultp= "Extreme depression")| Q(Resultp= "Severe depression")).filter(RelationshipStatus="fling").filter(
        Gender="male").count())
    ff = int(Personaldetails.objects.filter(Q(Resultp= "Extreme depression")| Q(Resultp= "Severe depression")).filter(RelationshipStatus="fling").filter(
        Gender="female").count())
    return render(request, 'portal/analysis/analysis5.html',{'mm':mm, 'mf': mf, 'sm': sm, 'sf': sf, 'ml': ml, 'fl': fl, 'mf': mf, 'ff': ff})

def analysis6(request):
    malep = int(Personaldetails.objects.filter(Gender='male').filter(
        Q(Resultp="Moderate depression") | Q(Resultp="Extreme depression") | Q(Resultp="Severe depression")).filter(Occupation__exact="Professional").count())
    femalep = int(Personaldetails.objects.filter(Gender='female').filter(
        Q(Resultp="Moderate depression") | Q(Resultp="Extreme depression") | Q(Resultp="Severe depression")).filter(Occupation__exact="Professional").count())
    maleb = int(Personaldetails.objects.filter(Gender='male').filter(
        Q(Resultp="Moderate depression") | Q(Resultp="Extreme depression") | Q(Resultp="Severe depression")).filter(
        Occupation__exact="Business").count())
    femaleb = int(Personaldetails.objects.filter(Gender='female').filter(
        Q(Resultp="Moderate depression") | Q(Resultp="Extreme depression") | Q(Resultp="Severe depression")).filter(
        Occupation__exact="Business").count())

    return render(request, 'portal/analysis/analysis6.html', {'malep': malep, 'femalep': femalep, 'maleb': maleb, 'femaleb': femaleb})


def stories(request):
    stories = Story.objects.filter(time__lte=timezone.now()).order_by('-likes','-time')
    return render(request, 'portal/stories.html', {'stories':stories})

def story_new(request):
    if request.method == "POST":
        form = StoryForm(request.POST)
        if form.is_valid():
            story = form.save(commit=False)
            story.time = timezone.now()
            story.sentiment=sentiment(story.story_text)
            story.save()
            return redirect('stories')
    else:
        form = StoryForm()
    return render(request, 'portal/new_story.html', {'form': form})

def story_detail(request, pk):
    story = get_object_or_404(Story, storyid=pk)
    return render(request, 'portal/story_detail.html', {'story': story})

def add_comment_to_story(request, pk):
    story = get_object_or_404(Story, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.story = story
            comment.save()
            return redirect('story_detail', pk=story.pk)
    else:
        form = CommentForm()
    return render(request, 'portal/add_comment_to_story.html', {'form': form,'story':story})

def like_story(request):
    story_id = None
    if request.method == 'GET':
        story_id = request.GET['story_id']

    likes = 0
    if story_id:
        story = Story.objects.get(storyid=int(story_id))
        if story:
            likes = story.likes + 1
            story.likes =  likes
            story.save()

    return HttpResponse(likes)
