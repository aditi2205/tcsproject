# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-13 07:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0034_auto_20170713_1231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='story',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='portal.Story'),
        ),
    ]