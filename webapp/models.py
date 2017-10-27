# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

#class people(models.Model):
 #   first_name = models.CharField(max_length = 20)
  #  last_name = models.CharField(max_length = 20)
   # email = models.CharField(max_length = 30)
    #home_town = models.CharField(max_length= 20)s
    #gender = models.CharField(max_length=1)
    #password = models.CharField(max_length = 20)
    #date_of_birth = models.DateField()
    

class Photos(models.Model):
    caption = models.CharField(max_length=255, blank=True)
    photo_data = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User)
    
class Friend(models.Model):
    users = models.ManyToManyField(User)                    #friends of current user
    current_user = models.ForeignKey(User, related_name='owner', null = True)  #current user field
    
    @classmethod
    def make_friend(cls, current_user, new_friend):
        friend, created = cls.objects.get_or_create(
                current_user=current_user
                )
        friend.users.add(new_friend)
        
    @classmethod
    def lose_friend(cls, current_user, new_friend):
        friend, created = cls.objects.get_or_create(
                current_user=current_user
                )
        friend.users.remove(new_friend)