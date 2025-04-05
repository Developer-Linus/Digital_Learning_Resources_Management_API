from rest_framework import serializers
from .models import CustomUser, Profile

# Serializer for the CustomUser model
class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email']
        read_only_fields = ['email']

#Serializer for the Profile Model
class ProfileSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer(read_only=True)
    class Meta:
        model = Profile
        fields = ['id', 'first_name', 'last_name', 'user', 'bio', 'phone_number', 'profile_picture']
        
        