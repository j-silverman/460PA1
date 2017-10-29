# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from webapp.forms import SignUpForm, PhotoForm, AlbumForm
from webapp.models import Photos, Friend, Album
from django.template import RequestContext, Context
from django.shortcuts import render_to_response
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User

def index(request):
    args = {'user': request.user}
    return render(request, 'home.html', args)

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

def profile(request, username):
    albums = Album.objects.all()
    documents = Photos.objects.all()
    user = User.objects.get(username=username)
    cuser = User.objects.get(username=request.user)
    friend = Friend.objects.get(current_user=request.user)
    friends = friend.users.all()
    args = {'documents':documents, 'albums':albums, 'user': user, 'friends':friends, 'cuser':cuser }
    return render(request, 'profile.html', args)

def picture(request, document):
    document = Photos.objects.get(caption=document)
    args = {'document':document}
    return render(request, 'picture.html', args)

#def get_user_profile(request):


def model_form_upload(request):
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            stock = form.save(commit=False)
            stock.author = request.user
            stock.save()
            return HttpResponseRedirect('')
    else:
        form = PhotoForm()
    return render(request, 'model_form_upload.html', {'form':form})

def album_upload(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST)
        if form.is_valid():
            stock = form.save(commit=False)
            stock.a_author = request.user
            stock.save()
            return HttpResponseRedirect('')
    else:
        form = AlbumForm()
    return render(request, 'album_upload.html', {'form':form})

def album_list(request, username):
    if request.method == 'GET':
        user = User.objects.get(username=username)
        documents = Photos.objects.all()
        #albums = Album.objects.all()
        albums = Album.objects.filter(a_author = user)
        args = {'user':user, 'documents':documents, 'albums': albums}
    return render(request, 'album_list.html', args)

  

def change_friends(request, operation, pk):
    user = User.objects.get(username=request.user)
    args = {'user': user}
    new_friend = User.objects.get(pk=pk)
    if operation == 'add':
        Friend.make_friend(request.user, new_friend)
    elif operation == 'remove':
        Friend.lose_friend(request.user, new_friend)
    return render(request, 'home.html', args)
    

