from django.contrib import admin
from .models import Post, Comment


# all about administration site
@admin.register(Post)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish', 'status')  # Display the list of given tuple value
    list_filter = ('status', 'created', 'publish', 'author')  # Display the filter value of given tuple
    search_fields = ('title', 'body')  # For searching
    prepopulated_fields = {'slug': ('title', ), }  # Prepopulate the slug field
    raw_id_fields = ('author', )  # Change the author widget
    date_hierarchy = 'publish'  # Create navigation date hierarchy
    ordering = ('status', 'publish')  # Post are ordering by status and publish


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'post', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name', 'email', 'body')
