# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.
class Personaldetails(models.Model):
	Pid = models.AutoField(primary_key=True)
	Name=models.CharField(max_length=20)


	GENDER=(
	 ('male','male'),
    ( 'male','female'),
    )

	Gender=models.CharField(max_length=20,choices=GENDER)

	RELATIONSHIP_STATUS=(
	 ('Single','Single'),
    ( 'Married','Married'),
    ('live_in_relationship','live_in_relationship'),
    ( 'fling','fling')
    )

	RelationshipStatus=models.CharField(max_length=20,choices=RELATIONSHIP_STATUS,)#single,married etc

	OCCUPATION=(
	 ('Student','Student'),
	 ('Profession','Profession'),
	 ('Employment','Employment'),
	 ('Business','Business')
		)

	Occupation=models.CharField(max_length=20,choices=OCCUPATION)#Student,working etc

	STUDENT=(
	('School','School'),
	('College','College'),
	)

	Student=models.CharField(max_length=20,choices=STUDENT )#college,school etc

	City=models.CharField(max_length=20)
	Age=models.IntegerField()
	Email_id=models.EmailField(max_length=50,null=True,blank=True)

class Responses(models.Model):
	#id= models.ForeignKey(Personaldetails, primary_key=True)
	id= models.AutoField(Personaldetails,primary_key=True)
	CHOICE=(
		(0,0),
		(1,1),
		(2,2),
		(3,3)
	)

	q1= models.IntegerField(choices=CHOICE)

	q2= models.IntegerField(choices=CHOICE)

	q3= models.IntegerField(choices=CHOICE)

	q4= models.IntegerField(choices=CHOICE)

	q5= models.IntegerField(choices=CHOICE)


class Result(models.Model):
	Rid= models.AutoField(Personaldetails, primary_key=True)
	result= models.IntegerField()


class Story(models.Model):
	 storyid=models.AutoField(primary_key=True)
	 name=models.CharField(max_length=50)
	 age=models.IntegerField()
	 location=models.CharField(max_length=30)
	 story_text=models.TextField()
	 time=models.DateTimeField(blank=True, null=True)

	 def publish(self):
		 self.Time = timezone.now()
		 self.save()

	 def __str__(self):
		return self.name+', '+str(self.age)
