# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Personaldetails(models.Model):
	Pid = models.AutoField(primary_key=True, unique=True)
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

	Student=models.CharField(max_length=20,choices=STUDENT, null=True,  blank=True )#college,school etc
	
	City=models.CharField(max_length=20)
	Age=models.IntegerField(null=True)
	Email_id=models.EmailField(max_length=20,null=True,blank=True)

	#def __str__(self):
          #  return self.Pid + '-' + self.Name


class Responses(models.Model):
	id= models.ForeignKey(Personaldetails, primary_key=True)
	CHOICE=(
		( 'option1',0),
		('option2',1),
		( 'option3',2),
		( 'option4',3)
	)

	q1= models.IntegerField(choices=CHOICE, null=True, blank=True)

	q2= models.IntegerField(choices=CHOICE, null=True, blank=True)

	q3= models.IntegerField(choices=CHOICE, null=True, blank=True)

	q4= models.IntegerField(choices=CHOICE, null=True, blank=True)

	q5= models.IntegerField(choices=CHOICE, null=True, blank=True)


class Result(models.Model):
	Rid= models.ForeignKey(Personaldetails, primary_key=True)
	result= models.IntegerField(null=True)


class Forum(models.Model):
	 fid=models.AutoField(primary_key=True)
	 Name=models.CharField(max_length=20)
	 Story=models.CharField(max_length=20)

