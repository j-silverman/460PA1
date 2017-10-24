# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from webapp.models import people

# Register your models here.

class PeopleAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name')

admin.site.register(people, PeopleAdmin)