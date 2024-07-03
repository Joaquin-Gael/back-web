from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.utils import timezone
from django.contrib.auth import (authenticate, login, logout)
from rest_framework import (viewsets, views, permissions, status, response, decorators)
from . import (serializers, models)
from users.serializers import (UserSerializer, User)

# Create your views here.

class PostsViews(viewsets.ModelViewSet):
    queryset = models.Post.objects.all()
    serializer_class = serializers.SerializerPost
    permission_classes = [permissions.AllowAny]

    @decorators.action(['GET'], detail=True, url_path='file')
    def get_file(self, request, pk=1):
        try:
            file = models.FilePost.objects.filter(post=pk)
            serializer = serializers.SerializerFilePost(file, many=True)
            return response.Response(serializer.data)
        except Exception as err:
            print(err.__class__, '------------------------')
            return response.Response({'Not Found Relation':err.args},status=status.HTTP_400_BAD_REQUEST)
    
    @decorators.action(['GET'], detail=True, url_path='likes')
    def get_likes(self, request, pk=1):
        try:
            likes = models.Like.objects.filter(post=pk)
            serializer = serializers.SerializerLike(likes, many=True)
            return response.Response(serializer.data)
        except Exception as err:
            print(err.__class__, '------------------------')
            return response.Response({'Not Found Relation':err.args},status=status.HTTP_400_BAD_REQUEST)
    
    @decorators.action(['GET'], detail=True, url_path='user')
    def get_user(self, rquest, pk=1):
        try:
            post = models.Post.objects.get(id=pk)
            user = User.objects.get(id=post.user.id)
            serializer = UserSerializer(user)
            return response.Response(serializer.data)
        except models.Post.DoesNotExist as err:
            print(err.__class__, '------------------------')
            return response.Response({'Not Found Relation':err.args},status=status.HTTP_400_BAD_REQUEST)
        except Exception as err:
            print(err.__class__, '------------------------')
            return response.Response({'Not Found Relation':err.args},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @decorators.action(['GET'], detail=True, url_path='comments')
    def get_comments(self, request, pk=1):
        try:
            comments = models.Comment.objects.filter(post=pk)
            serializer = serializers.SerializerComment(comments, many=True)
            return response.Response(serializer.data)
        except Exception as err:
            print(err.__class__, '------------------------')
            return response.Response({'Not Found Relation':err.args},status=status.HTTP_400_BAD_REQUEST)

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