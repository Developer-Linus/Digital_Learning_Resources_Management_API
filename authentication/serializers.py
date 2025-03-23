from rest_framework import serializers
# Module for settings of allauth
from allauth.account import app_settings as allauth_settings
# Module for sending email verification to user
from allauth.account.utils import send_email_confirmation
from django.contrib.auth import get_user_model
from allauth.account.models import EmailAddress

User = get_user_model()

# User Registration serializer
class UserRegistrationSerializer(serializers.ModelSerializer):
    # Include a custom field, password2 for validating the password
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True},
        }
        
    #Validate the the two passwords provided match
    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({'password': 'Passwords fields did not match'})
        return attrs
    
    # Override the create method to create a user
    def create(self, validated_data):
        del validated_data['password2']  # Remove password2 from the validated data
        user = User.objects.create_user(
            username=validated_data['username'], 
            email=validated_data['email'], 
            password=validated_data['password'])
        
        send_email_confirmation(self.context['request'], user)
        return user
        #Send email confirmation to the user
        send_email_confirmation(self.context['request'], user)
        
        return user
        
# User login serializer
class CustomLoginSerializer(serializers.Serializer):
    # Define two fields to be used for user authentication
    email = serializers.EmailField()
    password = serializers.CharField(style={'input_type': 'password'})
    
    # Define validation logic
    def validate(self, data):
        # Retrieve email and password from input data
        email = data.get('email')
        password = data.get('password')
        
        try:
            user = EmailAddress.objects.get(email=email).user
        except EmailAddress.DoesNotExist:
            raise serializers.ValidationError('Email or password is invalid.')
        if not user.is_active:
            raise serializers.ValidationError('Account is not active.')
        if not user.check_password(password):
            raise serializers.ValidationError('Email or password is invalid.')
        return {'user': user}
        
        
    
    
    
    
        