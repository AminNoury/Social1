from django.contrib import admin
from .models import Post, Comment, Vote

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'slug', 'body', 'created', 'updated']
    search_fields = ['slug', 'body']
    list_filter = ['created']
    prepopulated_fields = {'slug': ['body']}
    raw_id_fields = ['user']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'post', 'created', 'body', 'is_reply']
    raw_id_fields = ['user', 'post', 'reply']

admin.site.register(Vote)