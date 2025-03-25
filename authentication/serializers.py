from rest_framework import serializers
from django.contrib.auth import get_user_model


User = get_user_model()

class UserRegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    
    class Meta:
        model = User
        fields = ['email', 'password', 'password2']
        
        extra_kwargs = {
            'password': {'write_only': True},
        }
    def validate(self, attrs):
        if attrs['password']!= attrs['password2']:
            return serializers.ValidationError('Password fields did not match.')
        return attrs
    def create(self, validated_data):
        user = User.objects.create_user(
            email= validated_data['email'],
            password = validated_data['password']
        )
        
        return {
            'user': user,
        }