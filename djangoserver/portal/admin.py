# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Personaldetails, Responses, Result, Story,Comment


admin.site.register(Personaldetails)
admin.site.register(Responses)
admin.site.register(Result)
admin.site.register(Story)
admin.site.register(Comment)
