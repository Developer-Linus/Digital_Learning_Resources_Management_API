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
class CategoryDeleteAPIView(OwnerQuerySetMixin, CustomDeleteResponseMixin, generics.DestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = serializers.CategorySerializer
    
# View for Listing Resources
class ResourceListAPIView(OwnerQuerySetMixin, CustomListResponseMixin, generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = serializers.ResourceSerializer
    
# View for creating a resource
class ResourceCreateAPIView(OwnerCreateMixin, CreateResponseMixin, generics.CreateAPIView):
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
class LearningLogCreateAPIView(OwnerCreateMixin, CreateResponseMixin, generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = serializers.LearningLogSerializer
    
# View for retrieving learning logs
class LearningLogListAPIView(OwnerQuerySetMixin,CustomListResponseMixin, generics.ListAPIView):
    serializer_class = serializers.LearningLogSerializer
    permission_classes = [permissions.IsAuthenticated]

# View to reterive a learning log
class LearningLogDetailAPIView(OwnerCreateMixin, OwnerQuerySetMixin, CustomRetrieveResponseMixin, generics.RetrieveAPIView):
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

# View for creating a resource status
class ResourceStatusCreateAPIView(OwnerCreateMixin, CreateResponseMixin, generics.CreateAPIView):
    serializer_class = serializers.ResourceStatusSerializer
    permission_classes = [permissions.IsAuthenticated]

# View for listing resources status
class ResourceStatusListAPIView(OwnerQuerySetMixin, CustomListResponseMixin, generics.ListAPIView):
    serializer_class = serializers.ResourceStatusSerializer
    permission_classes = [permissions.IsAuthenticated]

# View for Retrieving a resource status
class ResourceStatusDetailAPiView(OwnerQuerySetMixin, CustomRetrieveResponseMixin, generics.RetrieveAPIView):
    serializer_class = serializers.ResourceStatusSerializer
    permission_classes = [permissions.IsAuthenticated]

# View for updating a resource status
class ResourceStatusUpdateAPIView(OwnerQuerySetMixin, CustomUpdateResponseMixin, generics.UpdateAPIView):
    serializer_class = serializers.ResourceStatusSerializer
    permission_classes = [permissions.IsAuthenticated]

# View for deleting a resource status instance
class ResourceStatusDeleteAPIView(OwnerQuerySetMixin, CustomDeleteResponseMixin, generics.DestroyAPIView):
    serializer_class = serializers.ResourceStatusSerializer
    permission_classes = [permissions.IsAuthenticated]
    
# View for bookmarking a resource
class BookmarkCreateAPIView(OwnerCreateMixin, CreateResponseMixin, generics.CreateAPIView):
    serializer_class = serializers.BookmarkSerializer
    permission_classes = [permissions.IsAuthenticated]

# View for Listing Bookmarks
class BookmarkListAPIView(OwnerQuerySetMixin, CustomListResponseMixin, generics.ListAPIView):
    serializer_class = serializers.BookmarkSerializer
    permission_classes = [permissions.IsAuthenticated]

# View for retrieving a specific bookmark
class BookmarkDetailAPIView(OwnerQuerySetMixin, CustomRetrieveResponseMixin, generics.RetrieveAPIView):
    serializer_class = serializers.BookmarkSerializer
    permission_classes = [permissions.IsAuthenticated]

# View for deleting a Bookmark
class BookmarkDeleteAPIView(OwnerQuerySetMixin, CustomDeleteResponseMixin, generics.DestroyAPIView):
    serializer_class = serializers.BookmarkSerializer
    permission_classes = [permissions.IsAuthenticated]


    
    
    
    
    