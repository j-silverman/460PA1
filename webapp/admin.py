# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from webapp.models import Photos, Friend, Album, Comment

# Register your models here.

#class PeopleAdmin(admin.ModelAdmin):
 #   list_display = ('first_name','last_name')

#admin.site.register(people, PeopleAdmin)

class PhotoAdmin(admin.ModelAdmin):
    list_display = ('caption', 'uploaded_at')
    
admin.site.register(Photos, PhotoAdmin)

admin.site.register(Friend)

admin.site.register(Album)

admin.site.register(Comment)