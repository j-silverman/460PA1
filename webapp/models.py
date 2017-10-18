# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class people(models.Model):
    first_name = models.CharField(max_length = 20)
    last_name = models.CharField(max_length = 20)
    email = models.CharField(max_length = 30)
    home_town = models.CharField(max_length= 20)
    gender = models.CharField(max_length=1)
    password = models.CharField(max_length = 20)
    date_of_birth = models.DateField()
    
