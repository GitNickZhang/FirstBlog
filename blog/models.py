from django.db import models
from django.contrib import admin

# Create your models here.
class BlogPost(models.Model):
	title = models.CharField(max_length=150)
	body = models.TextField()
	time = models.DateTimeField()

class User(models.Model):
	username = models.CharField(max_length=50)
	password = models.CharField(max_length=50)

class Comment(models.Model):
	username = models.CharField(max_length=20)
	comment = models.TextField()