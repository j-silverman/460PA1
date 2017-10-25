# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from webapp.forms import SubmitPerson
from webapp.models import people
from django.template import RequestContext, Context
from django.shortcuts import render_to_response

def index(request):
    return render(request, 'webapp/home.html')

#def register(request):
    #return render(request, 'webapp/register.html')

def login(request):
    return render(request, 'webapp/login.html')

def register(request):
    if request.method == 'POST':
        form = SubmitPerson(request.POST)
        if form.is_valid():
            my_model = people()
            my_model.first_name = request.POST.get('first_name','')
            my_model.last_name = request.POST.get('last_name','')
            my_model.email = request.POST.get('email', '')
            my_model.home_town = request.POST.get('home_town', '')
            my_model.gender = request.POST.get('gender', '')
            my_model.password = request.POST.get('password', '')
            my_model.date_of_birth = request.POST.get('date_of_birth','')
            my_model.save()
            return HttpResponse("submitted")
    else:
        form = SubmitPerson()
 
    return render(request, 'register.html')