# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-04 11:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0023_auto_20170630_0910'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personaldetails',
            name='Occupation',
            field=models.CharField(choices=[('Professional', 'Professional'), ('Business', 'Business'), ('NA', 'Not Applicable')], max_length=20),
        ),
        migrations.AlterField(
            model_name='personaldetails',
            name='Student',
            field=models.CharField(choices=[('School', 'School'), ('College', 'College'), ('NA', 'Not Applicable')], max_length=20),
        ),
    ]
