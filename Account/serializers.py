import datetime

from django.utils import timezone
from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],

            last_login=timezone.now()
        )
        validated_data.pop('password', None)

        return user

    # Remove the password field from the response
    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret.pop('password', None)

        return ret
