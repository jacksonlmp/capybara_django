from django.contrib import admin

from blog.models import BlogPost

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'created_at',
        'created_by',
        'published_at',
        'published_by',
        'is_premium',
    ]
    list_filter = [
        'is_premium',
        'created_at',
        'published_at',
    ]
    search_fields = [
        'title',
        'body',
        'created_by__username',
        'published_by__username',
    ]