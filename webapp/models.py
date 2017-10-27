# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


class Photos(models.Model):
    caption = models.CharField(max_length=255, blank=True)
    photo_data = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    author = models.ForeignKey(User)

# class Users(models.Model):
