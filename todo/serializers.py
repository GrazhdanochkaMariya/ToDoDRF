from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Task


# Serializer for Task model
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


# Serializer for User model
class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=6, write_only=True)
    first_name = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'first_name', 'last_name']
