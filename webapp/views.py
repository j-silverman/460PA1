# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from webapp.forms import SignUpForm
from webapp.models import people
from django.template import RequestContext, Context
from django.shortcuts import render_to_response
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User

def index(request):
    return render(request, 'home.html')

#def register(request):
    #return render(request, 'webapp/register.html')

def user_login(request):
    context = RequestContext(request)
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password = password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect('')
            else:
                return HttpResponse("Your account is disabled")
        else:
            return HttpResponse("Invalid username or password")
    else:
        return render(request, 'login.html', {})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(request, username=username, password=raw_password)
            login(request, user)
            return HttpResponse("submitted")
    else:
        form = SignUpForm()
 
    return render(request, 'register.html', {'form':form})

def profile(request):
    args = {'user': request.user}
    return render(request, 'profile.html', args)

