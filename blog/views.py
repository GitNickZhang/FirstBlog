#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from blog.models import BlogPost, User
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.contrib.auth.forms import UserCreationForm
from django import forms


# Create your views here.


def index(req):
    return render(req, 'content.html', {'User': 'Nick'})


def page(req):
    post_list = BlogPost.objects.all()
    paginator = Paginator(post_list, 2)
    num_pages = paginator.num_pages
    pages = range(1, num_pages + 1)
    width = num_pages * 34

    # Make sure page request is an int. If not, deliver first page.
    try:
        page = int(req.GET.get('page', '1'))
    except ValueError:
        page = 1

    # If page request (9999) is out of range, deliver last page of results.
    try:
        posts = paginator.page(page)
    except (EmptyPage, InvalidPage):
        posts = paginator.page(paginator.num_pages)

    return render(req, 'content.html', {
        'User': 'Nick',
        'pages': pages,
        'current_page': int(page),
        'width': width,
        'posts': posts,
    })


class UserForm(forms.Form):
    username = forms.CharField(label='用户名：', max_length=100)
    password = forms.CharField(label='密码：', widget=forms.PasswordInput())


# def register(request):
#     if request.method == 'GET':
#         userform = UserForm(request.GET)
#         if userform.is_valid():
#             username = userform.cleaned_data['username']
#             password = userform.cleaned_data['password']

#             user = User()
#             user.username = username
#             user.password = password
#             user.save()

#             return render_to_response('success.html', {'username': username})
#     else:
#         userform = UserForm()
#     return render_to_response('register.html', {'userform': userform})


# def login(request):
#     if request.method == 'GET':
#         userform = UserForm(request.GET)
#         if userform.is_valid():
#             username = userform.cleaned_data['username']
#             password = userform.cleaned_data['password']

#             user = User.objects.filter(
#                 username__exact=username, password__exact=password)
#             if user:
#                 return render_to_response('success.html', {'username': username})
#             else:
#                 return HttpResponseRedirect('/login/')
#     else:
#         userform = UserForm()
#     return render_to_response('login.html', {'userform': userform})

def register(req):
    if req.method == 'POST':
        form = UserCreationForm(req.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponse('Success')
    else:
        form = UserCreationForm()
    return render(req, 'registration/register.html', {'form': form})
