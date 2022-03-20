from dataclasses import fields
from rest_framework import serializers
from djoser.serializers import UserCreateSerializer

from django.contrib.auth import get_user_model

User = get_user_model()

class UserCreationSerializer(UserCreateSerializer):
    
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ['id', 'email', "first_name", "last_name", "password"]

    