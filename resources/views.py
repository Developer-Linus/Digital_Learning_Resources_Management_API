from rest_framework import generics, permissions, status
from . import serializers
from rest_framework.response import Response

# Custom mixins
from .mixins import (OwnerCreateMixin,
                     CreateResponseMixin,
                     OwnerQuerySetMixin,
                     CustomListResponseMixin,
                     CustomRetrieveResponseMixin,
                     CustomUpdateResponseMixin,
                     CustomDeleteResponseMixin)

# View for creating a Resource category
class CategoryCreateAPIView(CreateResponseMixin, OwnerCreateMixin, generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = serializers.CategorySerializer
        
# View for viewing existing categories
class CategoryListAPIView(OwnerQuerySetMixin, CustomListResponseMixin, generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = serializers.CategorySerializer
    
# view for deleting a category
class CategoryDeleteAPIView(OwnerQuerySetMixin,CustomDeleteResponseMixin, generics.DestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer = serializers.CategorySerializer
    
# View for Listing Resources
class ResourceListAPIView(OwnerQuerySetMixin, CustomListResponseMixin, generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = serializers.ResourceSerializer
    
# View for creating a resource
class ResourceCreateAPIView(OwnerCreateMixin, generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = serializers.ResourceSerializer

# View for retrieving a single resource
class ResourceDetailAPIView(OwnerQuerySetMixin, CustomRetrieveResponseMixin, generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = serializers.ResourceSerializer
    
# View for updating a resource
class ResourceUpdateAPIView(OwnerQuerySetMixin, CustomUpdateResponseMixin, generics.UpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = serializers.ResourceSerializer

# View for deleting a resource
class ResourceDeleteAPIView(OwnerQuerySetMixin, CustomDeleteResponseMixin, generics.DestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = serializers.ResourceSerializer

# View for creating  a Learning Log
class LearningLogCreateAPIView(OwnerCreateMixin, generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = serializers.LearningLogSerializer
    
# View for retrieving learning logs
class LearningLogListAPIView(OwnerQuerySetMixin,CustomListResponseMixin, generics.ListAPIView):
    serializer_class = serializers.LearningLogSerializer
    permission_classes = [permissions.IsAuthenticated]

# View to reterive a learning log
class LearningLogDetailAPIView(OwnerCreateMixin, CustomRetrieveResponseMixin, generics.RetrieveAPIView):
    serializer_class = serializers.LearningLogSerializer
    permission_classes = [permissions.IsAuthenticated]
    
# view for Updating a learning log
class LearningLogUpdateAPIView(OwnerQuerySetMixin, CustomUpdateResponseMixin, generics.UpdateAPIView):
    serializer_class = serializers.LearningLogSerializer
    permission_classes = [permissions.IsAuthenticated]
    
# View for deleting a learning log
class LearningLogDeleteAPIView(OwnerQuerySetMixin, CustomDeleteResponseMixin, generics.DestroyAPIView):
    serializer_class = serializers.LearningLogSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    
    
    
    