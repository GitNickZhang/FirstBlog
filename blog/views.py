#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from blog.models import BlogPost, User
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm, SetPasswordForm, PasswordChangeForm
from django.contrib.auth.views import login, logout
from django.contrib import auth
from django import forms


# Create your views here.


def index(req):
    return render(req, 'content.html', {'User': 'Nick'})


def page(req):
	# 创建认证用的表单
	form = AuthenticationForm(req)

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
        'form': form,
    })




def register(req):
    if req.method == 'POST':
        form = UserCreationForm(req.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponse(new_user)
    else:
        form = UserCreationForm()
    return render(req, 'registration/login.html', {'form': form})
