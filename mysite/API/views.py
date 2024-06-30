from django.shortcuts import (render, redirect)
from rest_framework import (viewsets, views, permissions, status, response)
from django.utils import timezone
from . import (models, serializers)

# Create your views here.
class IndexAPI(views.View):
    def get(self,request,*args,**kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        messages = models.MessagesAPI.objects.all()
        return render(request,'index.html',{
            'date':timezone.now(),
            'messages':messages
        })

class LoginAPI(views.View):
    def get(self,request,*args,**kwargs):
        return render(request,'login.html')
    
    def post(self,request,*args,**kwargs):
        try:
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = models.User.objects.get(username=username)
        except:
            redirect('login')
        if user.is_superuser:
            user.login_date_set(request)
            return redirect('index')
        else:
            redirect('login')
            

class MessagesAPI(viewsets.ModelViewSet):
    queryset = models.MessagesAPI.objects.all()
    serializer_class = serializers.MessagesSerializer
    permission_classes = [permissions.AllowAny]