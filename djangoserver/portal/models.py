# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone


#class Cities(models.Model):
#	SNo=models.IntegerField(primary_key=True)
#	City= models.CharField(max_length=50)
#	State=models.CharField(max_length=50)

def __str__(self):
		return self.City
# Create your models here.
class Personaldetails(models.Model):
	Pid = models.AutoField(primary_key=True)
	Date = models.DateTimeField(auto_now_add=True)
	Name=models.CharField(max_length=20,verbose_name ='Your Name')



	GENDER=(
	 ('male','male'),
	( 'female','female'),
	('Other', 'Other')
	)

	Gender=models.CharField(max_length=20,choices=GENDER,verbose_name ='Select Your Gender')
	#Othergender=models.CharField(max_length=100,default='None',null=True,verbose_name ='Gender');

	RELATIONSHIP_STATUS=(
	 ('Single','Single'),
	( 'Married','Married'),
	('live_in_relationship','live_in_relationship'),
	( 'fling','fling')
	)

	RelationshipStatus=models.CharField(max_length=20,choices=RELATIONSHIP_STATUS,verbose_name ='Your Current Relationship Status')#single,married etc
	STUDENT = (
		('School', 'School'),
		('College', 'College'),
		('NA', 'Not Applicable')
	)

	Student = models.CharField(max_length=20, choices=STUDENT,verbose_name ='Student')  # college,school etc

	OCCUPATION=(
	 ('Professional','Professional'),
	 ('Business','Business'),
	 ('NA', 'Not Applicable')
	 )

	Occupation=models.CharField(max_length=20,choices=OCCUPATION,verbose_name ='Your Work')
	#Otheroccupation=models.CharField(max_length=100,default='None',null=True,verbose_name ='Occupation');  #Student,working etc


	City=models.CharField(max_length=20,verbose_name ='Enter the name of your city')
	#0thercity=models.CharField(max_length=100,default='None',null=True,verbose_name ='City')

	Age=models.IntegerField(verbose_name ='Your Age')
	Email_id=models.EmailField(max_length=50,null=True,blank=True,verbose_name ='Email Id ')
	Score= models.IntegerField(null=True,blank=True)
	Resultp= models.CharField(max_length=50,null=True,blank=True)

	def __str__(self):
		return self.Name;

class Responses(models.Model):
	person= models.ForeignKey(Personaldetails, primary_key=True,default=0)
	# id= models.AutoField(Personaldetails,primary_key=True)
	CHOICE1 = (
		(0,'I do not feel sad.'),
		(1,'I feel sad'),
		(2,'I am sad all the time and I cant snap out of it.'),
		(3,'I am so sad and unhappy that I cant stand it.')
		)

	CHOICE2 = (
		(0, 'I am not particularly discouraged about the future.'),
		(1, 'I feel discouraged about the future'),
		(2, 'I feel I have nothing to look forward to.'),
		(3, 'I feel the future is hopeless and that things cannot improve.')

		)

	CHOICE3 = (
		(0, 'I do not feel like a failure.'),
		(1, 'I feel I have failed more than the average person.'),
		(2, 'As I look back on my life, all I can see is a lot of failures.'),
		(3, 'I feel I am a complete failure as a person.')

		)
	CHOICE4 = (
		(0, 'I get as much satisfaction out of things as I used to.'),
		(1, 'I dont enjoy things the way I used to.'),
		(2, 'I dont get real satisfaction out of anything anymore.'),
		(3, 'I am dissatisfied or bored with everything.')

		)

	CHOICE5 = (
		(0, 'I dont feel particularly guilty.'),
		(1, ' I feel guilty a good part of the time.'),
		(2, 'I feel quite guilty most of the time.'),
		(3, 'I feel guilty all of the time.')

		)
	CHOICE6 = (
		(0, 'I dont feel I am being punished.'),
		(1, '  I feel I may be punished.'),
		(2, 'I expect to be punished.'),
		(3, 'I feel I am being punished.')

		)
	CHOICE7 = (
		(0, 'I dont feel disappointed in myself'),
		(1, 'I am disappointed in myself.'),
		(2, 'I am disgusted with myself.'),
		(3, 'I hate myself.')

		)
	CHOICE8 = (
		(0, 'I dont feel I am any worse than anybody else.'),
		(1, 'I am critical of myself for my weaknesses or mistakes.'),
		(2, 'I blame myself all the time for my faults.'),
		(3, 'I blame myself for everything bad that happens.')

		)
	CHOICE9 = (
		(0, 'I dont have any thoughts of killing myself.'),
		(1, 'I have thoughts of killing myself, but I would not carry them out.'),
		(2, 'I would like to kill myself.'),
		(3, 'I would kill myself if I had the chance.')

		)

	CHOICE10 = (
		(0, 'I dont cry any more than usual.'),
		(1, 'I cry more now than I used to.'),
		(2, ' I cry all the time now.'),
		(3, 'I used to be able to cry, but now I cant cry even though I want to.')

		)
	CHOICE11 = (
		(0, 'I am no more irritated by things than I ever was.'),
		(1, 'I am slightly more irritated now than usual.'),
		(2, ' I am quite annoyed or irritated a good deal of the time.'),
		(3, 'I feel irritated all the time. ')

		)

	CHOICE12 = (
		(0, 'I have not lost interest in other people.'),
		(1, 'I am less interested in other people than I used to be.'),
		(2, 'I have lost most of my interest in other people.'),
		(3, 'I have lost all of my interest in other people.')

		)
	CHOICE13 = (
		(0, 'I make decisions about as well as I ever could.'),
		(1, 'I put off making decisions more than I used to.'),
		(2, 'I have greater difficulty in making decisions more than I used to.'),
		(3, 'I cant make decisions at all anymore')

		)
	CHOICE14 = (
		(0, 'I dont feel that I look any worse than I used to.'),
		(1, 'I am worried that I am looking old or unattractive.'),
		(2, 'I feel there are permanent changes in my appearance that make me look unattractive .'),
		(3, 'I believe that I look ugly.')

		)

	CHOICE15 = (
		(0, 'I can work about as well as before.'),
		(1, 'It takes an extra effort to get started at doing something.'),
		(2, 'I have to push myself very hard to do anything.'),
		(3, ' I cant do any work at all. ')

		)


	CHOICE16 = (
		(0, 'I can sleep as well as usual.'),
		(1, 'I dont sleep as well as I used to.'),
		(2, 'I wake up 1-2 hours earlier than usual and find it hard to get back to sleep.'),
		(3, 'I wake up several hours earlier than I used to and cannot get back to sleep')

		)

	CHOICE17 = (
		(0, 'I dont get more tired than usual.'),
		(1, 'I get tired more easily than I used to'),
		(2, 'I get tired from doing almost anything.'),
		(3, 'I am too tired to do anything.')

		)
	CHOICE18 = (
		(0, 'My appetite is no worse than usual.'),
		(1, 'My appetite is not as good as it used to be.'),
		(2, 'My appetite is much worse now.'),
		(3, 'I have no appetite at all anymore.')

		)
	CHOICE19 = (
		(0, 'I havent lost much weight, if any, lately.'),
		(1, ' I have lost more than five pounds.'),
		(2, 'I have lost more than ten pounds.'),
		(3, 'I have lost more than fifteen pounds.')

		)
	CHOICE20 = (
		(0, 'I am no more worried about my health than usual.'),
		(1, ' I am worried about physical problems like aches, pains, upset stomach, or constipation.'),
		(2, 'I am very worried about physical problems and its hard to think of much else.'),
		(3, 'I am so worried about my physical problems that I cannot think of anything else.')

		)
	CHOICE21 = (
		(0, 'I have not noticed any recent change in my interest in sex.'),
		(1, 'I am less interested in sex than I used to be.'),
		(2, 'I have almost no interest in sex.'),
		(3, 'I have lost interest in sex completely.')

		)

	q1= models.IntegerField(choices=CHOICE1)

	q2= models.IntegerField(choices=CHOICE2)

	q3= models.IntegerField(choices=CHOICE3,null=True)

	q4= models.IntegerField(choices=CHOICE4,null=True)

	q5= models.IntegerField(choices=CHOICE5,null=True)
	q6 = models.IntegerField(choices=CHOICE6,null=True)
	q7 = models.IntegerField(choices=CHOICE7,null=True)
	q8 = models.IntegerField(choices=CHOICE8,null=True)
	q9 = models.IntegerField(choices=CHOICE9,null=True)
	q10 = models.IntegerField(choices=CHOICE10,null=True)
	q11 = models.IntegerField(choices=CHOICE11,null=True)
	q12 = models.IntegerField(choices=CHOICE12,null=True)
	q13 = models.IntegerField(choices=CHOICE13,null=True)
	q14 = models.IntegerField(choices=CHOICE14,null=True)
	q15 = models.IntegerField(choices=CHOICE15,null=True)
	q16 = models.IntegerField(choices=CHOICE16,null=True)
	q17 = models.IntegerField(choices=CHOICE17,null=True)
	q18 = models.IntegerField(choices=CHOICE18,null=True)
	q19 = models.IntegerField(choices=CHOICE19,null=True)
	q20 = models.IntegerField(choices=CHOICE20,null=True)
	q21 = models.IntegerField(choices=CHOICE21,null=True)
	result= models.IntegerField()

	def __str__(self):
		return str(self.person)

class Result(models.Model):
	Rid= models.ForeignKey(Personaldetails, primary_key=True,default=0)
	result= models.IntegerField()

	def __str__(self):
		return self.Rid+', '+str(self.result)


class Story(models.Model):
	 storyid=models.AutoField(primary_key=True)
	 name=models.CharField(max_length=50,default='Anonymous')
	 age=models.IntegerField(blank=False, null=False)
	 location=models.CharField(max_length=30,blank=False, null=False)
	 story_title=models.CharField(max_length=200,blank=False, null=False)
	 story_text=models.TextField(blank=False, null=False)
	 likes=models.IntegerField(default=0)
	 time=models.DateTimeField(blank=True, null=True)
	 email=models.EmailField(max_length=50,null=True,blank=True)
	 sentiment=models.IntegerField(default=0)

	 def publish(self):
		 self.time = timezone.now()
		 self.save()

	 def __str__(self):
		 return self.name+', '+str(self.age)

class Comment(models.Model):
    story = models.ForeignKey(Story, related_name='comment',null=True)
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text
