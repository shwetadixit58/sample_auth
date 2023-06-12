from rest_framework import serializers
from userauth.models import *

class UserRegistrationSerializer(serializers.ModelSerializer):

#we are writing this because we need to confirm password field in our registration request

    password2=serializers.CharField(style={'input_type':'password'}, write_only=True)
    class Meta:
        model= User
        fields = ['email', 'name', 'tc', 'password', 'password2']
        extra_kwagrs= {
            'password':{'write_only': True}
        }

    # validating password and confirm password while registration
    def validate(self,attrs):
        password = attrs.get('password')
        password2 = attrs.get('password2')
        if password != password2:
            raise serializers.ValidationError("password and confirm password not matching")
        return attrs

    def create(self, validate_data):
        return User.objects.create_user(**validate_data)

class UserLoginSerializer(serializers.ModelSerializer):
    email=serializers.EmailField(max_length=255)
    class Meta:
        model=User
        fields=['email', 'password']

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model= User
        fields = ['id','email','name']
