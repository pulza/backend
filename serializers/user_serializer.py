from rest_framework import serializers
from model.models import User
from django.contrib.auth.hashers import make_password
import re

class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(error_messages={'invalid': 'invalid_email'})

    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'password']
        extra_kwargs = {
            'password': {'write_only': True},
            'id': {'read_only': True}
        }


    def validate_name(self, name):
        if len(name) < 2: raise serializers.ValidationError('short_name')

        return name

    def validate_email(self, email):
        regex_email = '([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+'
        if not re.fullmatch(regex_email, email):
            raise serializers.ValidationError('invalid_email')

        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError('email_exists')

        return email

    def validate_password(self, password):
        if len(password) < 8: raise serializers.ValidationError('short_password')
        return password

    def create(self, validated_data):
        user = User.objects.create(name=validated_data['name'],
                                        email=validated_data['email'],
                                        password=make_password(validated_data['password']))
        return user
