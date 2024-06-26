from rest_framework import serializers
from posts.models import (Post, Comment, Like, FilePost)

class SerializerPost(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class SerializerComment(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class SerializerLike(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'

class SerializerFilePost(serializers.ModelSerializer):
    class Meta:
        model = FilePost
        fields = '__all__'