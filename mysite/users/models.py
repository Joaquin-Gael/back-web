from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.contrib.auth import (authenticate, login, logout)

# Create your models here.
class TypeUser(models.Model):
    type_user = models.TextChoices('type_user', 'admin user')
    type_user = models.CharField(max_length=150)
    date_joined = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'''
            {self.type_user},
            {self.date_joined}
        '''
    
    class Meta:
        db_table = 'type_users'
        verbose_name = 'TypeUser'
        verbose_name_plural = 'TypeUsers'
        ordering = ['id']
        
    def __unicode__(self):
        return self.type_user

class User(AbstractUser):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateField(auto_now_add=True)
    last_login = models.DateField(null=True, blank=True)
    last_logout = models.DateField(null=True, blank=True)
    type_user = models.ForeignKey(TypeUser, on_delete=models.CASCADE)

    def is_staff_user(self):
        return self.is_staff

    def login_date_set(self,request):
        self.last_login = timezone.now()
        self.save()
        login(request, authenticate(username=self.username, password=self.password))
    
    def logout_date_set(self):
        self.last_logout = timezone.now()
        self.save()
        logout(request)
    
    def __str__(self):
        return f'''
            {self.username},
            {self.email},
            {self.is_active},
            {self.date_joined},
            {self.last_login},
            {self.last_logout},
            {self.type_user}
        '''
    
    class Meta:
        db_table = 'users'
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        ordering = ['id']
        
    def __unicode__(self):
        return self.username