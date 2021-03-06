# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from webapp.forms import SignUpForm, PhotoForm, AlbumForm, CommentForm, TagForm, LoggedInCommentForm
from webapp.models import Photos, Friend, Album, Comment, Tag, Like
from django.template import RequestContext, Context
from django.shortcuts import render_to_response
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.db.models import Q, Count
from django.core.urlresolvers import reverse

def index(request):
    documents = Photos.objects.all()
    args = {'user': request.user, 'documents':documents}
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
    if request.user.is_authenticated:
        cuser = User.objects.get(username=request.user)
        friend, created = Friend.objects.get_or_create(current_user=request.user)
        friends = friend.users.all()
        args = {'documents':documents, 'albums':albums, 'user': user, 'friends':friends, 'cuser':cuser }
    else:
        args = {'documents':documents, 'albums':albums, 'user': user}
    return render(request, 'profile.html', args)

def picture(request, document):
    document = Photos.objects.get(caption=document)
    comments = Comment.objects.filter(picture_id=document)
    tags = Tag.objects.filter(photo_id=document)
    user = request.user         
    likes = Like.objects.filter(picture=document).count()   
    liked = Like.objects.filter(picture=document).values_list('l_user')
    liked = [int(x[0]) for x in liked]
    print(liked)
    args = {'document':document, 'comments':comments, 'tags':tags, 'user':user, 'likes':likes, 'liked':liked}
    return render(request, 'picture.html', args)

#def get_user_profile(request):


def model_form_upload(request):
    if request.method == 'POST':
        form = PhotoForm(request.user, request.POST, request.FILES)
        if form.is_valid():
            stock = form.save(commit=False)
            stock.author = request.user
            stock.save()
            return HttpResponseRedirect('')
    else:
        form = PhotoForm(request.user)
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
        c_user = request.user
        documents = Photos.objects.all()
        #albums = Album.objects.all()
        albums = Album.objects.filter(a_author = user)
        args = {'user':user, 'documents':documents, 'albums': albums, 'c_user':c_user}
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

def like(request, pk):
    photo = Photos.objects.get(pk = pk)
    cuser = request.user
    Like.objects.create(picture = photo, l_user = cuser)
    return HttpResponseRedirect(reverse('index'))

def add_comment_to_post(request, pk):
    photo = Photos.objects.get(pk=pk)
    puser = Photos.objects.only('author').get(pk=pk)
    print(puser)
    if request.user.is_authenticated:
        user = User.objects.get(username = request.user)
        if request.method == "POST":
            form = LoggedInCommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.picture = photo
                comment.author = user
                comment.save()
                return HttpResponseRedirect('')
        else:
            form = LoggedInCommentForm()
            args = {'form':form, 'puser':puser,'user':user}
        return render(request, 'add_comment_to_post.html', args)

    else:
        if request.method == "POST":
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.picture = photo
                comment.save()
                return HttpResponseRedirect('')
        else:
            form = CommentForm()
        return render(request, 'add_comment_to_post.html', {'form':form})

        form = CommentForm()
    return render(request, 'add_comment_to_post.html', {'form':form})




def search(request):
    query = request.GET.get("q")
    query1 = request.GET.get("qt")
    query2 = request.GET.get("qa")
    query3 = request.GET.get("qc")
    if query:
        queryset = User.objects.values_list('username', flat=True)
        queryset = queryset.filter(username__icontains = query)
        context = {'queryset':queryset}
        return render(request, 'search.html', context)
    elif query1:
        queryset1 = Tag.objects.filter(tag_text__icontains = query1)
        context = {'queryset1':queryset1}
        return render(request, 'search.html', context)
    elif query2:
        queryset2 = Album.objects.all()
        print(queryset2)
        queryset2 = queryset2.filter(album_name__icontains = query2)
        context = {'queryset2':queryset2}
        return render(request, 'search.html', context)
    elif query3:
        queryset3 = Comment.objects.filter(text__icontains = query3)
        print(queryset3)
        context = {'queryset3':queryset3}
        return render(request, 'search.html', context)
    else:
        return render(request, 'search.html')

def add_tag(request, pk):
    photo = Photos.objects.get(pk = pk)
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            tag = form.save(commit=False)
            tag.photo_id = photo
            tag.t_user = request.user
            tag.save()
            return HttpResponseRedirect('')
    else:
        form = TagForm()
    return render(request, 'add_tag.html', {'form':form})

def tag_list(request, tag):
    tags = Tag.objects.filter(tag_text = tag).values('photo_id')
    print(tags)
    if request.method == 'GET':
        documents = Photos.objects.filter(pk__in = tags)
        args = {'documents':documents, 'tag':tag}
    return render(request, 'tag_list.html', args)


def user_activity(request):
    tag_count = Tag.objects.all().values_list('tag_text').annotate(total = Count('tag_text')).order_by('-total')
    tag_count = [str(x[0]) for x in tag_count]
    context = {'tag_count':tag_count}
    return render(request, 'user_activity.html', context)

def useractivity1(request):
    authors = Photos.objects.all().values_list('author').annotate(total=Count('author')).order_by('-total')
    authors = authors.all()[:5]
    print(authors[0])
    author = [int(x[0]) for x in authors]
    users = User.objects.filter(pk__in=author)
    context = {'users':users}
    return render(request, 'thing.html', context)

def might_like(request):
    user = request.user
    your_tags = Tag.objects.filter(t_user = user)
    your_tags = your_tags.all().values_list('tag_text').annotate(total = Count('tag_text')).order_by('-total')
    print(your_tags)
    return render(request, 'might_like.html')

def delete_tag(request, pk):
    #if request.method == "POST":
    u = Tag.objects.get(pk=pk).delete()
    return HttpResponseRedirect(reverse('index'))    

def delete_photo(request, pk):
    u = Photos.objects.get(pk=pk).delete()
    return HttpResponseRedirect(reverse('index'))    

def delete_album(request, pk):
    u = Album.objects.get(pk=pk).delete()
    return HttpResponseRedirect(reverse('index')) 

def unlike(request, pk):
    user = request.user
    like = Like.objects.filter(l_user = user)
    u = like.get(picture=pk).delete()
    return HttpResponseRedirect(reverse('index'))
    

