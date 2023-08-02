from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    """Serializer for the Task model."""

    class Meta:
        """Meta for TaskSerializer."""

        model = Task
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    """Serializer for the User model."""

    password = serializers.CharField(min_length=6, write_only=True)
    first_name = serializers.CharField(required=True)

    class Meta:
        """Meta for UserSerializer."""

        model = User
        fields = ["username", "password", "first_name", "last_name"]

    def create(self, validated_data):
        """Create a new user instance with validated data."""
        password = validated_data.pop("password", None)
        instance = self.Meta.model(**validated_data)

        instance.is_active = True
        if password is not None:
            # Set password does the hash.
            instance.set_password(password)
        instance.save()
        return instance
