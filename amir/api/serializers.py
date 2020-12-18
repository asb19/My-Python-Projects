from posts.models import posts
from rest_framework.serializers import ModelSerializer

class PostSerializer(ModelSerializer):
    class Meta:
        model = posts
        fields=[
            'user',
            'title',
            'content',
            'photo',
            'timestamp'
        ]