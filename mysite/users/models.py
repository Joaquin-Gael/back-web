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
    type_user = models.ForeignKey(TypeUser, on_delete=models.CASCADE, null=True)

    def is_staff_user(self) -> bool:
        """RETORNA SI ES STAFF"""
        return self.is_staff

    def login_date_set(self,request,password) -> None:
        """SETA LA FECHA DE LOGIN Y GENERA LA SESSION"""
        self.last_login = timezone.now()
        self.save()
        login(request, authenticate(username=self.username, password=password))
    
    def logout_date_set(self,request) -> None:
        """SETEA LA FECHA DE LOGOUT Y CIERRA LA SESSION"""
        self.last_logout = timezone.now()
        self.save()
        logout(request)
    
    def get_likes_info(self) -> [object]:
        """RETORNA UN LISTADO DE LOS LIKES DEL USUARIO O UNA LISTA CON ERROR SI NO EXISTE EL MODELO
        try: 
            from posts.models import Like
            likes = Like.objects.filter(user=self)
            return likes
        except Exception as err:
            print('No existe el modelo Like', err.args)
            return ['No content',err.args]
        """
        try: 
            from posts.models import Like
            likes = Like.objects.filter(user=self)
            return likes
        except Exception as err:
            print('No existe el modelo Like', err.args)
            return ['No content',err.args]
    
    def __str__(self) -> str:
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
    
class Visit(models.Model):
    timestap = models.DateTimeField(auto_now_add=True)
    ip_addres = models.GenericIPAddressField()
    user_agent = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f'''
            {self.timestap},
            {self.ip_addres},
            {self.user_agent}
        '''
    
    class Meta:
        db_table = 'visits'
        verbose_name = 'Visit'
        verbose_name_plural = 'Visits'
        ordering = ['id']
        
    def __unicode__(self):
        return self.timestap

class WeeklyVisit(models.Model):
    week_start = models.DateField()
    week_end = models.DateField()
    visit_count = models.PositiveIntegerField(default=0)

    def __str__(self) -> str:
        return f'''
            {self.week_start},
            {self.week_end},
            {self.visit_count}
        '''

    class Meta:
        db_table = 'weekly_visits'
        verbose_name = 'WeeklyVisit'
        verbose_name_plural = 'WeeklyVisits'
        ordering = ['id']

    def __unicode__(self):
        return self.week_start