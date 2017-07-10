# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-10 05:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0029_auto_20170706_2314'),
    ]

    operations = [
        migrations.AddField(
            model_name='story',
            name='comments',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='story',
            name='likes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='story',
            name='story_title',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='story',
            name='name',
            field=models.CharField(default='Anonymous', max_length=50),
        ),
        migrations.AlterField(
            model_name='story',
            name='story_text',
            field=models.TextField(blank=True, null=True),
        ),
    ]
