from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Category model
class Category(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='category')
    name = models.CharField(max_length=30, null=False, blank=False, default='Uncategorized')
    description=models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.name

# Resource model
class Resource(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='resources')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='resources', default="General", null=False, blank=False)
    resource_name = models.CharField(max_length=255, null=False, blank=False)
    resource_author = models.CharField(max_length=200, null=False, blank=False)
    resource_url = models.URLField(max_length=300, null=False, blank=True)
    resource_image = models.ImageField(upload_to='resource_images/', null=True, blank=True)
    publication_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.resource_name} by {self.resource_author}'
    
# LearningLog Model
class LearningLog(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='logs')
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE, related_name='logs')
    notes = models.TextField(null=False, blank=False)
    review = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'Notes for {self.resource.resource_name} are {self.notes[:30]}...'

# Resource status model
class ResourceStatus(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='resource_status')
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE, related_name='status')
    in_progress = models.BooleanField(default=False)
    is_completed = models.BooleanField(default=False)
    date_completed = models.DateField(null=True, blank=True)
    is_important = models.BooleanField(default=False)
    
# Bookmark Model
class Bookmark(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookmarks')
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE, related_name='bookmarks')
    created_at = models.DateTimeField(auto_now_add=True)
    