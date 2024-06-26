from django.shortcuts import render
from django.views import View
from django.utils import timezone
from django.contrib.auth import (authenticate, login, logout)
from rest_framework import (viewsets, views, permissions, status, response)
from . import (serializers, models)

# Create your views here.

class UserViews(viewsets.ModelViewSet):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = [permissions.AllowAny]

class TypeUserViews(viewsets.ModelViewSet):
    queryset = models.TypeUser.objects.all()
    serializer_class = serializers.TypeUserSerializer
    permission_classes = [permissions.AllowAny]