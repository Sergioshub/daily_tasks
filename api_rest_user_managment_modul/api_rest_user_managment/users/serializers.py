from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from users.models import CustomUser, UsersContact


class CreateUserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)
    
    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'middle_name', 'last_name', 'email', 'password')

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        validate_password(password)
        instance.set_password(password)
        instance.save()
        return instance



class UserContactsSerializer(serializers.ModelSerializer):
    
    country_code = serializers.CharField(help_text="Код страны")
    phone_number = serializers.CharField(help_text="Номер телефона")

    class Meta:
        model = UsersContact
        fields = ['country_code', 'phone_number']

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['user'] = user
        return UsersContact.objects.create(**validated_data)


class CustomUserSerializer(serializers.ModelSerializer):
    
    contacts = UserContactsSerializer(many=True, read_only=True)

    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'first_name', 'last_name', 'middle_name', 'email', 'date_joined', 'contacts']