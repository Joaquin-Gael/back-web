from django.shortcuts import render
from rest_framework import (viewsets, views, permissions, status, response)
from django.utils import timezone
from . import (models, serializers)

# Create your views here.
class IndexAPI(views.View):
    def get(self,request,*args,**kwargs):
        messages = models.MessagesAPI.objects.all()
        return render(request,'index.html',{
            'date':timezone.now(),
            'messages':messages
        })

class MessagesAPI(viewsets.ModelViewSet):
    queryset = models.MessagesAPI.objects.all()
    serializer_class = serializers.MessagesSerializer
    permission_classes = [permissions.AllowAny]