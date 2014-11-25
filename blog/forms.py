#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.forms import ModelForm
from blog.models import Comment

# 设置表单元类来方便View里数据的存储
class CommentForm(ModelForm):
	class Meta:
		model = Comment