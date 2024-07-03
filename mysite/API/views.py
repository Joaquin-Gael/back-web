from django.shortcuts import (render, redirect)
from rest_framework import (viewsets, views, permissions, status, response)
from django.utils import timezone
from django.http import (HttpResponse, HttpResponseRedirect)

import users.models
from . import (models, serializers)
import users

# Create your views here.
class IndexAPI(views.View):
    def get(self,request,*args,**kwargs) -> HttpResponse:
        if not request.user.is_authenticated:
            return redirect('login')
        messages = models.MessagesAPI.objects.all()
        return render(request,'index.html',{
            'date':timezone.now(),
            'messages':messages
        })

class LoginAPI(views.View):
    def get(self,request,*args,**kwargs) -> HttpResponse:
        return render(request,'login.html')
    
    def post(self,request,*args,**kwargs) -> HttpResponseRedirect:
        try:
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = users.models.User.objects.get(username=username)
            if user.is_staff_user:
                user.login_date_set(request,password)
                print('paso')
                return redirect('index')
            else:
                print('no paso')
                return redirect('login')
        except:
            redirect('login')

class LogoutAPI(views.View):
    def get(self,request,*args,**kwargs) -> HttpResponseRedirect:
        try:
            user = request.user
            user.logout_date_set(request)
            return redirect('login')
        except:
            return redirect('login')

class UsersAPI(views.View):
    def get(self,request,*args,**kwargs) -> HttpResponse:
        if not request.user.is_authenticated:
            return redirect('login')
        try:
            users_list = users.models.User.objects.all()
            return render(request,'users.html',{
                'users':users_list
            })
        except:
            return render(request,'users.html',{
                'users':[]
            })
            

class MessagesAPI(viewsets.ModelViewSet):
    queryset = models.MessagesAPI.objects.all()
    serializer_class = serializers.MessagesSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]