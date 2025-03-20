from django.db import models
import uuid
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils.timezone import now
from phonenumber_field.modelfields import PhoneNumberField #Used for phone number validation

class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        # create and return a normal user
        if not email:
            raise ValueError('Email is required.')
        if not username:
            raise ValueError('Username is required.')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email)
        user.set_password(password)
        user.role = 'user' # Default role
        user.save(using=self._db)
        
        return user
    def create_superuser(self, username, email, password):
        # Create and return a superuser
        user = self.create_user(username, email, password)
        user.role = 'admin'
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user

# Create custom user model
class CustomUser(AbstractBaseUser, PermissionsMixin): 
    #Custom user model
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('user', 'User'),
    ]
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='user')
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False) # Required for django admin access
    
    objects = CustomUserManager()
    
    USERNAME_FIELD = 'email' # Authentication by email instead of django default username
    REQUIRED_FIELDS = ['username']
    
    def __str__(self):
        return self.username

# Create profile model extending custom user model
# -Stores extra user details without bloating CustomUser model
class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(blank=True, null=True)
    phone_number = PhoneNumberField(unique=True, null=True, blank=True)
    profile_picture = models.ImageField(upload_to='profiles/', null=True, blank=True)
    
    def __str__(self):
        return f'Profile of {self.user.username}'

    
    
    
    
        
