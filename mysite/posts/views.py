from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.utils import timezone
from django.contrib.auth import (authenticate, login, logout)
from rest_framework import (viewsets, views, permissions, status, response, decorators)
from . import (serializers, models)

# Create your views here.

class PostsViews(viewsets.ModelViewSet):
    queryset = models.Post.objects.all()
    serializer_class = serializers.SerializerPost
    permission_classes = [permissions.AllowAny]

    @decorators.action(['GET'], detail=True)
    def get_file(self, request, pk):
        try:
            file = models.FilePost.objects.filter(post=pk)
            serializer = serializers.SerializerFilePost(file, many=True)
            return response.Response(serializer.data)
        except Exception as err:
            print(err)
            return response.Response({'Not Found Relation':err},status=status.HTTP_400_BAD_REQUEST)

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