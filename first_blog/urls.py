#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url

from django.contrib import admin
import settings
from django.contrib.auth.views import login, logout
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'first_blog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    # 设置引用静态文件的路径
    url(r'^index/$', 'blog.views.page'),
    url(r'^login/$', login),
    url(r'^register/$', 'blog.views.register'),
    url(r'^logout/$', logout, {'template_name': 'index.html', 'next_page': '/index/'}),
)

