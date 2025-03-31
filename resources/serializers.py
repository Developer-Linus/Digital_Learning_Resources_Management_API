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
    owner = serializers.PrimaryKeyRelatedField(read_only=True)
    
    class Meta: 
        model = LearningLog
        fields = ['id', 'owner', 'resource', 'notes', 'review']
    
    def validate(self, attrs):
        resource = attrs.get('resource')
        notes = attrs.get('notes')
        review = attrs.get('review')
        
        instance = self.instance  # Get the current instance if updating
        
        if instance:
            # Exclude the current instance from the uniqueness check
            if LearningLog.objects.filter(resource=resource).exclude(id=instance.id).exists():
                raise serializers.ValidationError('A learning log for this resource already exists.')
        else:
            # Standard uniqueness check when creating a new log
            if LearningLog.objects.filter(resource=resource).exists():
                raise serializers.ValidationError('A learning log for this resource already exists.')
        
        if not notes or notes.isspace():
            raise serializers.ValidationError('Notes are required.')
        if len(review) > 350:
            raise serializers.ValidationError('Review is too long. Cannot exceed 350 characters.')
        return attrs

# Resource status serializer
class ResourceStatusSerializer(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = ResourceStatus
        fields = ['id', 'owner', 'resource', 'in_progress', 'is_completed', 'date_completed', 'is_important']
    # Validate in_progress and is_completed fields
    def validate(self, attrs):
        in_progress = attrs.get('in_progress')
        is_completed = attrs.get('is_completed')
        resource = attrs.get('resource')
        
        # Only check for uniqueness if creating a new instance
        if self.instance is None and ResourceStatus.objects.filter(resource=resource).exists():
            raise serializers.ValidationError({'resource': 'This resource already has a status.'})
        
    
        if not isinstance(in_progress, bool):
            raise serializers.ValidationError('In progress status must be a boolean value.')
        if not isinstance(is_completed, bool):
            raise serializers.ValidationError('Is completed status must be a boolean value.')
        if in_progress and is_completed:
            raise serializers.ValidationError('In_progress and is_completed cannot be True at the same time.') 
        return attrs
        

# Bookmark serializer 
class BookmarkSerializer(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(read_only=True)
    
    class Meta:
        model = Bookmark
        fields = ['id', 'owner', 'resource', 'created_at']
        read_only_fields = ['id', 'created_at']
    
    # check that a user cannot bookmark same resource more than once
    def validate(self, attrs):
        resource = attrs.get('resource')
        
        instance = self.instance
        if Bookmark.objects.filter(resource = resource).exists():
            raise serializers.ValidationError('Resource already bookmarked.')
        
        return attrs
   