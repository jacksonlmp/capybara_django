from rest_framework.response import Response 
from rest_framework.generics import ListAPIView

from blog.models import BlogPost
from blog.serializers import BlogPostSerializer

class BlogPostList(ListAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    