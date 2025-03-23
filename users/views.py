from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import Profile
from .serializers import ProfileSerializer

from drf_spectacular.utils import extend_schema


# Class-based view for retrieving user's profile
@extend_schema(
    responses={200: ProfileSerializer, 404: {'error': 'Profile not found.'}}
)
class ProfileView(APIView):
    def get(self, request):
        # Get's user profile
        try:
            profile = Profile.objects.get(user=request.user)
            serializer = ProfileSerializer(profile)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Profile.DoesNotExist:
            return Response({'error' : 'Profile not found.'},status=status.HTTP_404_NOT_FOUND)

# Class-based view for updating user's profile
@extend_schema(
    request=ProfileSerializer,
    responses={200: ProfileSerializer, 400: {'error': 'Invalid request data'}, 404: {'error': 'Profile not found.'}}
)
class UpdateProfileView(APIView):
    def put(self, request):
        #Get user's profile
        try:
            profile = Profile.objects.get(user=request.user)
            serializer = ProfileSerializer(profile, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Profile.DoesNotExist:
            return Response({'errors':'Profile not found.'}, status=status.HTTP_200_OK)

# Class-based view for deleting user's profile
@extend_schema(
    responses={200: {'message': 'Profile successfully deleted'}, 404: {'error': 'Profile not found.'}}
)
class DeleteProfileView(APIView):
    def delete(self, request):
        # Get user's profile
        try:
            profile = Profile.objects.get(user=request.data)
            profile.delete()
            return Response ({'message' : 'Profile successfully deleted'},status=status.HTTP_200_OK )
        except Profile.DoesNotExist:
            return Response({'error' : 'Profile not found.'}, status=status.HTTP_404_NOT_FOUND)
