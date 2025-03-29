from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils.timezone import now
from phonenumber_field.modelfields import PhoneNumberField #Used for phone number validation
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from rest_framework_simplejwt.tokens import RefreshToken

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, superuser=False):
        # create and return a normal user
        if not email:
            raise ValueError('Email is required.')
        try:
            validate_email(email)  # Check if the email format is valid
        except ValidationError:
            raise ValueError('Invalid email format.')  # Raise an error for invalid emails
        
        
        email = self.normalize_email(email)
        user = self.model(email=email)
        user.set_password(password)
        
        if superuser: # If it's a superuser set special flags before saving in database
            user.role = 'admin'
            user.is_superuser=True
            user.is_staff=True
        else:
            user.role='user' #Default role
        
        user.set_password(password)
        user.save(using=self._db)
        
        return user
    def create_superuser(self, email, password):
        return self.create_user(email, password, superuser=True)
    
# Create custom user model
class CustomUser(AbstractBaseUser, PermissionsMixin): 
    #Custom user model
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('user', 'User'),
    ]
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='user')
    is_verified = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False) # Required for django admin access
    
    objects = CustomUserManager()
    
    USERNAME_FIELD = 'email' # Authentication by email instead of django default username
    REQUIRED_FIELDS = []
    
    def __str__(self):
        return self.email
    
    def tokens(self):
        refresh = RefreshToken.for_user(self)
        tokens = {
            'access': str(refresh.access_token),
            'refresh': str(refresh)
        }
        return tokens

# Create profile model extending custom user model
# -Stores extra user details without bloating CustomUser model
class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='profile')
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    bio = models.TextField(blank=True, null=True)
    phone_number = PhoneNumberField(unique=True, null=True, blank=True)
    profile_picture = models.ImageField(upload_to='profiles/', null=True, blank=True)
    
    def __str__(self):
        return f'Profile of {self.user.email}'
    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

    
    
    
    
        
