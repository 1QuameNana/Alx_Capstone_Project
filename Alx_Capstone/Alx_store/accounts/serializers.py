from rest_framework import serializers
from django.contrib.auth import authenticate, get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','email','username']
        read_only_fields =['is_active','is_staff','date_joined']

class CreateUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)


    class Meta:
        model = User
        fields = ['email','username']
        def create(self, validated_data):
            user =User(email =validated_data['email'],
                       username =validated_data['username'])
            user.set_password(validated_data['password'])
            user.save()
            return user
            


