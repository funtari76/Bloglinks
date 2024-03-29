""" Admin file for bloglinks app """
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Bloglinks, Comment


@admin.register(Bloglinks)
class BloglinksAdmin(SummernoteModelAdmin):
    """ Summernote admin class """

    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_on')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)
# admin.site.register(Bloglinks)
# admin.site.register(Comment)
