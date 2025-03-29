from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics, permissions
from .models import Profile
from .serializers import ProfileSerializer

class ProfileViewMixin:
    def get_object(self):
        # Return the user's profile
        return self.request.user.profile

class ProfileDetailAPIView(ProfileViewMixin, generics.RetrieveAPIView):
    # Ensure that only authenticated users can access this view
    permission_classes = (permissions.IsAuthenticated,)
    # Specify the serializer to use for this view
    serializer_class = ProfileSerializer

class ProfileUpdateAPIView(ProfileViewMixin, generics.UpdateAPIView):
    # Ensure that only authenticated users can access this view
    permission_classes = (permissions.IsAuthenticated,)
    # Specify the serializer to use for this view
    serializer_class = ProfileSerializer

class ProfileDeleteAPIView(ProfileViewMixin, generics.DestroyAPIView):
    # Ensure that only authenticated users can access this view
    permission_classes = (permissions.IsAuthenticated,)