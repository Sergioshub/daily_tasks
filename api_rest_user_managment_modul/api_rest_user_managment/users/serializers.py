from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from .models import CustomUser, UsersContact
from django.urls import reverse
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED


class UserContactSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = UsersContact
        fields = ['country_code', 'phone_number']


class CustomUserSerializer(serializers.ModelSerializer):

    contacts = UserContactSerializer(many=True, read_only=True)
    password = serializers.CharField(write_only=True, style={'input_type': 'password'})

    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'first_name', 'last_name', 'middle_name', 'email', 'password', 'contacts']  
  
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        validate_password(password)
        instance.set_password(password)
        instance.save()
        # return Response(status=HTTP_201_CREATED, reverse('rest_framework:login')})
        return instance