from rest_framework import serializers
from .models import Category, Resource, LearningLog, ResourceStatus, Bookmark
from users.serializers import CustomUserSerializer
from django.core.validators import URLValidator # Validating URL link
from django.core.exceptions import ValidationError
import datetime


# Category Serializer
class CategorySerializer(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(read_only=True) 
    class Meta:
        model = Category
        fields = ['id', 'owner', 'name', 'description']
    # Validate category name
    def validate_name(self, value):
        if not value:
            raise serializers.ValidationError('Category name cannot be empty.')
        request = self.context.get('request')  # Get request from serializer context
        if request and request.user.is_authenticated:
            if Category.objects.filter(owner=request.user, name=value).exists():  # Use .exists()
                raise serializers.ValidationError('Category with this name already exists.')
        return value
    # Validate category description
    def validate_description(self, value):
        if len(value)>300:
            raise serializers.ValidationError('Category description cannot exceed 300 characters.')
        return value

# Resource Serializer
class ResourceSerializer(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(read_only=True)
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    class Meta:
        model = Resource
        fields = ['id', 'owner', 'category', 'resource_name', 'resource_author', 'resource_url', 'resource_image', 'publication_date', 'created_at']
    # validate resource name - not empty
    def validate_name(self, value):
        if not value.strip():
            raise serializers.ValidationError('Resource name must be provided.')
        return value
    # validate URL link
    def validate_resource_url(self, value):
        try:
            url = URLValidator()(value)
        except ValidationError:
            raise serializers.ValidationError('Invalide resource URL.')
        return value
    # Validate resource pubication date
    def validate_publication_date(self, value):
        if value > datetime.date.today():
            raise serializers.ValidationError('Publication date cannot be in future.')
        return value
        
        
# Learning Log serializer
class LearningLogSerializer(serializers.ModelSerializer):
    owner = CustomUserSerializer(read_only=True)
    resource = ResourceSerializer(read_only=True)
    
    class Meta: 
        model = LearningLog
        fields = ['id', 'owner', 'resource', 'notes', 'review']
        read_only_fields = ['id']
    # validae notes and review
    def validate(self, attrs):
        notes = attrs['notes']
        review = attrs['review']
        
        if not notes:
            raise serializers.ValidationError('Notes are required.')
        if len(review) > 350:
            raise serializers.ValidationError('Review is too long. Cannot exceed 350 characters.')
        return attrs

# Resource status serializer
class ResourceStatusSerializer(serializers.ModelSerializer):
    owner = CustomUserSerializer(read_only=True)
    resource = ResourceSerializer(read_only=True)
    
    class Meta:
        model = ResourceStatus
        fields = ['id', 'owner', 'resource', 'in_progress', 'is_completed', 'date_completed', 'is_important']
        read_only_fields = ['id']
    # Validate in_progress and is_completed fields
    def validate(self, attrs):
        in_progress = attrs['in_progress']
        is_completed = attrs['is_completed']
        
        if not isinstance(in_progress, bool):
            raise serializers.ValidationError('In progress status must be a boolean value.')
        if not isinstance(is_completed, bool):
            raise serializers.ValidationError('Is completed status must be a boolean value.')
        raise attrs
        

# Bookmark serializer 
class BookmarkSerializer(serializers.ModelSerializer):
    owner = CustomUserSerializer(read_only=True)
    resource = ResourceSerializer(read_only=True)
    
    class Meta:
        model = Bookmark
        fields = ['id', 'owner', 'resource', 'created_at']
        read_only_fields = ['id', 'created_at']
    
    # check resource validity
    def validate_resource(self, value):
        try:
            Resource.objects.get(id=value.id)
        except Resource.DoesNotExist:
            raise serializers.ValidationError('Invalid resource')
        return value