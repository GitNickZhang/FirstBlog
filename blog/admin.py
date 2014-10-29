from django.contrib import admin
from blog.models import BlogPost
# Register your models here.

class BlogPostAdmin(admin.ModelAdmin):
	list_display = ('title', 'time')

admin.site.register(BlogPost, BlogPostAdmin)