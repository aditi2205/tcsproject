from django import forms
from django.contrib.auth.models import User
from django.conf import settings
from .models import Personaldetails,Responses

class DetailsForm(forms.ModelForm):
	class Meta:
         model=Personaldetails
         fields=['Pid','Name','Gender','RelationshipStatus','Occupation','Student','City','Age','Email_id']
       


class Quiz(forms.ModelForm):
	class Meta:
         model=Responses
         fields=['q1','q2','q3','q4','q5']