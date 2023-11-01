# Django rest
from rest_framework import generics

# Models
from apps.blogs.models import Post

# Serializers
from apps.blogs.serializers import PostSerializer


class PostListAPIView(generics.ListCreateAPIView):
    """Post list API view."""

    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    """Post detail API view."""

    queryset = Post.objects.all()
    serializer_class = PostSerializer
