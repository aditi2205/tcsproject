from django import forms
from django.contrib.auth.models import User
from django.conf import settings
from .models import Personaldetails,Responses, Story, Comment

class DetailsForm(forms.ModelForm):
    Name=forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Type your name here','id':'id_name'}))
    City=forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Type your City here','id':'id_city'}))
    #Email_id=forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'For notifications (optional)','id':'id_email'}))



    class Meta:
         model=Personaldetails
         fields=['Pid','Name','Gender','RelationshipStatus','Occupation','Student','City','Age','Email_id']



class Quiz(forms.ModelForm):
    class Meta:
         model=Responses
         fields=['q1','q2','q3','q4','q5','q6','q7','q8','q9','q10','q11','q12','q13','q14','q15','q16','q17','q18','q19','q20','q21']

         #label=['q1.ques1','ques2','q3','q4','q5','q6','q7','q8','q9','q10','q11','q12','q13','q14','q15','q16','q17','q18','q19','q20','q21']
         #labels = {
          #  'q1': ('Writer'),
        #}

#
# class Quiz2(forms.ModelForm):
#   class Meta:
#          model=Responses
#          fields=['q2']
#          exclude=['q1','q3','q4','q5','q6','q7','q8','q9','q10','q11','q12','q13','q14','q15','q16','q17','q18','q19','q20','q21']
#
# class Quiz3(forms.ModelForm):
#   class Meta:
#          model=Responses
#          fields=['q3']
#          exclude=['q1','q2','q4','q5','q6','q7','q8','q9','q10','q11','q12','q13','q14','q15','q16','q17','q18','q19','q20','q21']
#
# class Quiz4(forms.ModelForm):
#   class Meta:
#          model=Responses
#          fields=['q4']
#          exclude=['q1','q2','q3','q5','q6','q7','q8','q9','q10','q11','q12','q13','q14','q15','q16','q17','q18','q19','q20','q21']
#
# class Quiz5(forms.ModelForm):
#   class Meta:
#          model=Responses
#          fields=['q5']
#          exclude=['q1','q2','q3','q4','q6','q7','q8','q9','q10','q11','q12','q13','q14','q15','q16','q17','q18','q19','q20','q21']
#
# class Quiz6(forms.ModelForm):
#   class Meta:
#          model=Responses
#          fields=['q6']
#          exclude=['q1','q2','q3','q4','q5','q7','q8','q9','q10','q11','q12','q13','q14','q15','q16','q17','q18','q19','q20','q21']
#
# class Quiz7(forms.ModelForm):
#   class Meta:
#          model=Responses
#          fields=['q7']
#          exclude=['q1','q2','q3','q4','q5','q6','q8','q9','q10','q11','q12','q13','q14','q15','q16','q17','q18','q19','q20','q21']
#
# class Quiz8(forms.ModelForm):
#   class Meta:
#          model=Responses
#          fields=['q8']
#          exclude=['q1','q2','q3','q4','q5','q6','q7','q9','q10','q11','q12','q13','q14','q15','q16','q17','q18','q19','q20','q21']
#
# class Quiz9(forms.ModelForm):
#   class Meta:
#          model=Responses
#          fields=['q9']
#          exclude=['q1','q2','q3','q4','q6','q7','q8','q5','q10','q11','q12','q13','q14','q15','q16','q17','q18','q19','q20','q21']
#
# class Quiz10(forms.ModelForm):
#   class Meta:
#          model=Responses
#          fields=['q10']
#          exclude=['q1','q2','q3','q4','q5','q7','q8','q9','q6','q11','q12','q13','q14','q15','q16','q17','q18','q19','q20','q21']
#
# class Quiz11(forms.ModelForm):
#   class Meta:
#          model=Responses
#          fields=['q11']
#          exclude=['q1','q2','q3','q4','q5','q7','q8','q9','q10','q6','q12','q13','q14','q15','q16','q17','q18','q19','q20','q21']
#
# class Quiz12(forms.ModelForm):
#   class Meta:
#          model=Responses
#          fields=['q12']
#          exclude=['q1','q2','q3','q4','q5','q7','q8','q9','q10','q11','q6','q13','q14','q15','q16','q17','q18','q19','q20','q21']
#
# class Quiz13(forms.ModelForm):
#   class Meta:
#          model=Responses
#          fields=['q13']
#          exclude=['q1','q2','q3','q4','q5','q7','q8','q9','q10','q11','q12','q6','q14','q15','q16','q17','q18','q19','q20','q21']
#
# class Quiz14(forms.ModelForm):
#   class Meta:
#          model=Responses
#          fields=['q14']
#          exclude=['q1','q2','q3','q4','q5','q7','q8','q9','q10','q11','q12','q13','q6','q15','q16','q17','q18','q19','q20','q21']
#
# class Quiz15(forms.ModelForm):
#   class Meta:
#          model=Responses
#          fields=['q15']
#          exclude=['q1','q2','q3','q4','q5','q7','q8','q9','q10','q11','q12','q13','q14','q6','q16','q17','q18','q19','q20','q21']
#
# class Quiz16(forms.ModelForm):
#   class Meta:
#          model=Responses
#          fields=['q16']
#          exclude=['q1','q2','q3','q4','q5','q7','q8','q9','q10','q11','q12','q13','q14','q15','q6','q17','q18','q19','q20','q21']
#
# class Quiz17(forms.ModelForm):
#   class Meta:
#          model=Responses
#          fields=['q17']
#          exclude=['q1','q2','q3','q4','q5','q7','q8','q9','q10','q11','q12','q13','q14','q15','q16','q6','q18','q19','q20','q21']
#
# class Quiz18(forms.ModelForm):
#   class Meta:
#          model=Responses
#          fields=['q18']
#          exclude=['q1','q2','q3','q4','q5','q7','q8','q9','q10','q11','q12','q13','q14','q15','q16','q17','q6','q19','q20','q21']
#
# class Quiz19(forms.ModelForm):
#   class Meta:
#          model=Responses
#          fields=['q19']
#          exclude=['q1','q2','q3','q4','q5','q7','q8','q9','q10','q11','q12','q13','q14','q15','q16','q17','q18','q6','q20','q21']
#
# class Quiz20(forms.ModelForm):
#   class Meta:
#          model=Responses
#          fields=['q20']
#          exclude=['q1','q2','q3','q4','q5','q7','q8','q9','q10','q11','q12','q13','q14','q15','q16','q17','q18','q19','q6','q21']
#
# class Quiz21(forms.ModelForm):
#   class Meta:
#          model=Responses
#          fields=['q21']
#          exclude=['q1','q2','q3','q4','q5','q7','q8','q9','q10','q11','q12','q13','q14','q15','q16','q17','q18','q19','q20','q6']
#




class StoryForm(forms.ModelForm):

    class Meta:
        model = Story
        fields = ('name','age','location','email','story_title','story_text')

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)
