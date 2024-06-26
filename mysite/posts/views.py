from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.utils import timezone
from django.contrib.auth import (authenticate, login, logout)
from rest_framework import (viewsets, views, permissions, status, response)
from . import (serializers, models)

# Create your views here.

class PostsViews(viewsets.ModelViewSet):
    queryset = models.Post.objects.all()
    serializer_class = serializers.SerializerPost
    permission_classes = [permissions.AllowAny]

class CommentViews(viewsets.ModelViewSet):
    queryset = models.Comment.objects.all()
    serializer_class = serializers.SerializerComment
    permission_classes = [permissions.AllowAny]

class LikeViews(viewsets.ModelViewSet):
    queryset = models.Like.objects.all()
    serializer_class = serializers.SerializerLike
    permission_classes = [permissions.AllowAny]

class FilePostViews(viewsets.ModelViewSet):
    queryset = models.FilePost.objects.all()
    serializer_class = serializers.SerializerFilePost
    permission_classes = [permissions.AllowAny]