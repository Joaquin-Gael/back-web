from rest_framework import serializers
from API.models import MessagesAPI

class MessagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = MessagesAPI
        fields = '__all__'