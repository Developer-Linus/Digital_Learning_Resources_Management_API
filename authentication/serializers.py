from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import TokenError


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
class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()
    
    def validate(self, attrs):
        try: 
            self.token = RefreshToken(attrs['refresh'])
        except TokenError:
            raise serializers.ValidationError('Invalid or expired token.')
        return attrs
    
    def save(self, **kwargs):
        try:
            RefreshToken(self.token).blacklist()
        except TokenError:
            serializers.ValidationError('Invalid or Expired token.')
        