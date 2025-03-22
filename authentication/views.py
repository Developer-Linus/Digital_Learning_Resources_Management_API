from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserRegistrationSerializer
from dj_rest_auth.registration.views import RegisterView

from dj_rest_auth.registration.views import SocialLoginView
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client

class UserRegistrationView(APIView):
    # Define POST request to register a new user
    def post(self, request):
        # Create a serializer instance with request data
        serializer = UserRegistrationSerializer(data=request.data, context={'request':request})
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'User registered successfully. Please verify your email address.'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter
    callback_url = "http://localhost:3000/"
    client_class = OAuth2Client
