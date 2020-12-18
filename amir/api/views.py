from django.shortcuts import render
from posts.models import posts
from .serializers import PostSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
# Create your views here.

class PostView(ModelViewSet):
    queryset=posts.objects.all().order_by('-timestamp')
    serializer_class=PostSerializer