# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models import Q

class Album(models.Model):
    album_name = models.CharField(max_length=50, blank = True)
    date_created = models.DateTimeField(auto_now_add = True)
    date_modified = models. DateTimeField(auto_now = True)
    a_author = models.ForeignKey(User)
    
    def __str__(self):
        return self.album_name

class Photos(models.Model):
    caption = models.CharField(max_length=255, blank=True)
    photo_data = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User)
    album_id = models.ForeignKey(Album)

    def __str__(self):
        return self.caption

class Tag(models.Model):
    tag_text = models.CharField(max_length = 20, blank = True)
    photo_id = models.ForeignKey(Photos)
    t_user = models.ForeignKey(User)

    def __str__(self):
        return self.tag_text

class Comment(models.Model):
    picture = models.ForeignKey(Photos, null = True)
    album = models.ForeignKey(Album, null = True)
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add =True)



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
