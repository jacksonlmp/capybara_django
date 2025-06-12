from rest_framework import serializers
from blog.models import BlogPost

class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = [
            'title',
            'body',
            'is_premium',
            'created_at',
            'created_by',
            'published_at',
            'published_by',
            'updated_at'
        ]
