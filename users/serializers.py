from rest_framework import serializers
from .models import CustomUser, Profile

# Serializer for the CustomUser model
class CustomUserSerializer(serializers.ModelSerializer):
    # Ensure only non-sensitive data are exposed
    class Meta:
        model = CustomUser
        fields = ['id', 'email']
        read_only_fields = ['email']

#Serializer for the Profile Model
class ProfileSerializer(serializers.ModelSerializer):
    # Used for retrieving and updating user profile
    user = CustomUserSerializer(read_only=True)
    class Meta:
        model = Profile
        fields = ['user', 'bio', 'phone_number', 'profile_picture']
        
        