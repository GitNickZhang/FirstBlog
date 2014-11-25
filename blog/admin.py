from django.contrib import admin
from blog.models import BlogPost, User, Comment
# Register your models here.

class BlogPostAdmin(admin.ModelAdmin):
	list_display = ('title', 'time')

class UserAdmin(admin.ModelAdmin):
	list_display = ('username',)

class CommentAdmin(admin.ModelAdmin):
	list_display = ('username', 'comment')

admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Comment, CommentAdmin)