# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Personaldetails, Responses, Result


admin.site.register(Personaldetails)
admin.site.register(Responses)
admin.site.register(Result)
