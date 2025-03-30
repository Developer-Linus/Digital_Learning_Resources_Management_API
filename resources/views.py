from rest_framework import generics, permissions, status
from . import serializers
from .models import Resource, LearningLog, ResourceStatus, Bookmark, Category
from rest_framework.response import Response
from .mixins import OwnerCreateMixin  # Import the mixin

# View for creating a Resource category
class CategoryCreateAPIView(OwnerCreateMixin, generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = serializers.CategorySerializer
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            return Response(
                {
                    'status': 'success',
                    'message': 'Category created successfully.',
                    'data': serializer.data
                }, status=status.HTTP_201_CREATED
            )
        
        return Response(
            {'status': 'error',
             'message': 'Category creation failed.',
             'errors': serializer.errors}, 
            status=status.HTTP_400_BAD_REQUEST
        )
        
# View for viewing existing categories
class CategoryListAPIView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = serializers.CategorySerializer
    def get_queryset(self):
        user = self.request.user
        qs = Category.objects.filter(owner=user)
        return qs
    def list(self, request, *args, **kwargs):
        try:
            queryset = self.get_queryset()
            if not queryset.exists():
                return Response(
                    {'status': 'error',
                     'message': 'You have created no resources.'},
                    status=status.HTTP_404_NOT_FOUND
                )
            serializer = self.serializer_class(queryset, many=True)
            return Response(
                {'status': 'success',
                 'message': 'Categories retrieved successfully',
                 'data': serializer.data},
                status=status.HTTP_200_OK
            )
        except Exception as e:
            return Response(
                {'status': 'error',
                 'message': 'An error occurred while retrieving your categories'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
# view for deleting a category
class CategoryDeleteAPIView(generics.DestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer = serializers.CategorySerializer
    
    def get_queryset(self):
        return Category.objects.filter(owner=self.request.user)
    
    def delete(self, request, *args, **kwargs):
            # Get category to delete
            instance = self.get_object() # Handles 404 error automatically.
            # Delete the category
            self.perform_destroy(instance)
            return Response(
                {'status': 'success',
                 'messasge': 'Category deleted successfully.'},
                status=status.HTTP_200_OK
            )
# View for Listing Resources
class ResourceListAPIView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = serializers.ResourceSerializer
    
    def get_queryset(self):
        return Resource.objects.filter(owner=self.request.user)
    def list(self, request, *args, **kwargs):
        try:
            queryset = self.get_queryset()
            if not queryset.exists():
                return Response(
                    {'status': 'error', 'message':'No resources found. Please create some resources.'}, 
                    status=status.HTTP_404_NOT_FOUND,
                )
            serializer = self.get_serializer(queryset, many=True)
            return Response(
                {'status': 'success',
                 'message': 'Resources retrieved successfully.',
                 'data': serializer.data},
                status=status.HTTP_200_OK,
            ) 
        except Exception as e:
            return Response(
                {'status': 'error',
                 'messsage': 'An error occured while retrieving resources.',
                 'details': str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
# View for creating a resource
class ResourceCreateAPIView(OwnerCreateMixin, generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = serializers.ResourceSerializer
        
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            return Response(
                {'status': 'success',
                 'message': 'Resource created successfully.',
                 'data': serializer.data}, 
                status=status.HTTP_201_CREATED
            )
        return Response(
            {'status': 'error',
             'message': 'Resource creation failed.',
             'errors': serializer.errors},
            status=status.HTTP_400_BAD_REQUEST
        )

# View for retrieving a single resource
class ResourceDetailAPIView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = serializers.ResourceSerializer
    
    def get_queryset(self):
        return Resource.objects.filter(owner=self.request.user)
    
    def retrieve(self, request, *args, **kwargs):
        # Get the object instance
        instance = self.get_object()
        # Serialize the object retrieved
        serializer = self.get_serializer(instance)
        return Response(
            {'status': 'success',
             'message': 'Resource retrieved successfully.',
             'data': serializer.data
             },
            status=status.HTTP_200_OK
        )
# View for updating a resource
class ResourceUpdateAPIView(generics.UpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = serializers.ResourceSerializer
    
    def get_queryset(self):
        return Resource.objects.filter(owner=self.request.user)
    
    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        return Response(
            {'status': 'success',
             'message': 'Resource updated successfully.',
             'data': response.data},
            status=status.HTTP_200_OK
        )

# View for deleting a resource
class ResourceDeleteAPIView(generics.DestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = serializers.ResourceSerializer
    
    def get_queryset(self):
        return Resource.objects.filter(owner=self.request.user)
    
    def delete(self, request, *args, **kwargs):
        try:
            # Get the specific object to delete
            instance = self.get_object()
            # Perform deletion
            self.perform_destroy(instance)
            return Response(
                {'status': 'success',
                 'message': 'Resource deleted successfully.'},
                status=status.HTTP_200_OK
            )
        except Exception as  e:
            return Response(
                {'status': 'error',
                 'message': 'An error while trying to delete the resource.'},
                status=status.HTTP_400_BAD_REQUEST
            )