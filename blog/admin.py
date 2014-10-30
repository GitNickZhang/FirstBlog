from django.contrib import admin
from blog.models import BlogPost, User
# Register your models here.

class BlogPostAdmin(admin.ModelAdmin):
	list_display = ('title', 'time')

class UserAdmin(admin.ModelAdmin):
	list_display = ('username',)

admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(User, UserAdmin)