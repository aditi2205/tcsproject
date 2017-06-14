# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Details(models.Model):
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
	
	Student=models.CharField(max_length=20,choices=STUDENT)#college,school etc
	
	City=models.CharField(max_length=20)
	Age=models.IntegerField(null=True)
	Email_id=models.EmailField(max_length=20,blank=True)
	
class Forum(models.Model):
	 fid=models.AutoField(primary_key=True)
	 Name=models.CharField(max_length=20)
	 Story=models.CharField(max_length=20)

