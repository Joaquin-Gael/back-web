from rest_framework import serializers
from users.models import (User, TypeUser, Visit, WeeklyVisit)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['groups', 'user_permissions', 'first_name', 'last_name', 'last_login', 'is_staff', 'is_superuser','last_logout']
    
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        user.is_superuser = False
        user.is_staff = False
        user.is_active = True
        user.save()
        return user
    
    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return self

class TypeUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeUser
        fields = '__all__'

class VisitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visit
        fields = '__all__'

class WeeklyVisitSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeeklyVisit
        fields = '__all__'