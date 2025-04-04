from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import TokenError
from django.contrib.auth import authenticate
from rest_framework.exceptions import AuthenticationFailed


User = get_user_model()

# User registration serializer
class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    confirm_password = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'confirm_password']
        
        extra_kwargs = {
            'password': {'write_only': True},
        }
    def validate(self, attrs):
        if len(attrs['password'])<8:
            return serializers.ValidationError('Password must be at least 8 characters.')
        if attrs['password']!= attrs['confirm_password']:
            return serializers.ValidationError('Password fields did not match.')
        return attrs
    def create(self, validated_data):
        user = User.objects.create_user(
            email= validated_data['email'],
            password = validated_data['password']
        )
        return user

# Serializer for login
class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255)
    password = serializers.CharField(style={'input_type': 'password'}, max_length=68, write_only=True)
    tokens = serializers.CharField(max_length=555, read_only=True)
    class Meta:
        model = User
        fields = ['email', 'password', 'tokens']

    
    def validate(self, attrs):
        email = attrs.get('email', '')
        password = attrs.get('password', '')
        
        user = authenticate(email=email, password=password)
        
        if not user:
            raise AuthenticationFailed('Invalid login credentials.')
        if not user.is_active:
            raise AuthenticationFailed('Account disabled. Please contact admin.')
        if not user.is_verified:
            raise AuthenticationFailed('Email not verified. Request a new verification link.')
        return {'email': user.email,
                'tokens': user.tokens
                }
    
# Serializer for logout
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

# Serializer for email verification
class EmailVerificationSerializer(serializers.ModelSerializer):
    token = serializers.CharField(max_length=555)
    class Meta:
        model = User
        fields = ['token']
        