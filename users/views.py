from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics, permissions
from .models import Profile
from .serializers import ProfileSerializer
from .mixins import ProfileViewMixin

# View for viewing the profile - user must be authenticated
class ProfileDetailAPIView(ProfileViewMixin, generics.RetrieveAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = ProfileSerializer

# View for updating profile - user must be authenticated
class ProfileUpdateAPIView(ProfileViewMixin, generics.UpdateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = ProfileSerializer

# View for deleting a profile - user must be authenticated
class ProfileDeleteAPIView(ProfileViewMixin, generics.DestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)