# Django rest
from rest_framework import serializers

# Models
from apps.blogs.models import Post


class PostSerializer(serializers.ModelSerializer):
    """Post serializer."""

    class Meta:
        """Meta class."""

        model = Post
        fields = '__all__'
        read_only_fields = ('id', 'created', 'modified')
