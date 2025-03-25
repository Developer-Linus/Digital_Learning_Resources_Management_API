from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserRegistrationSerializer, CustomLoginSerializer
# from dj_rest_auth.registration.views import RegisterView
from rest_framework_simplejwt.tokens import RefreshToken

from drf_spectacular.utils import extend_schema

from dj_rest_auth.registration.views import SocialLoginView
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client

# User Registration view
@extend_schema(
    request=UserRegistrationSerializer,
    responses={201: {'message': 'User registered successfully. Please verify your email address.'}, 400: {'error': 'Invalid request data'}}
)
class UserRegistrationView(APIView):
    # Define POST request to register a new user
    def post(self, request):
        # Create a serializer instance with request data
        serializer = UserRegistrationSerializer(data=request.data, context={'request':request})
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'User registered successfully. Please verify your email address.'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# User login view
@extend_schema(
    request=CustomLoginSerializer,
    responses={200: {
        'access':'string',
       'refresh':'string',
       'message':'string'
    }, 400: {'error': 'Invalid request data'}}
)
class LoginView(APIView):
    def post(self, request):
        serializer = CustomLoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            refresh = RefreshToken.for_user(user)
            return Response(
                {
                'access': str(refresh.access_token),
                'refresh': str(refresh),
                'message': 'You have logged in successfully.',
                }
                )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Logout View
@extend_schema(
    request={'refresh': {'type':'string', 'description': 'Refresh token'}},
    responses={
        200: {'message': {'type':'string', 'description': 'Logout message'}},
        400: {'message': {'type':'string', 'description': 'Error message'}}
    }
)
class LogoutView(APIView):
    def post(self, request):
        refresh_token = request.data.get('refresh')
        if refresh_token:
            try:
                token = RefreshToken(refresh_token)
                token.blacklist()
                return Response({'message': 'You have logged out successfully.'}, status=status.HTTP_200_OK)
            except Exception as e:
                return Response({'message': 'Invalid refresh token'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'message': 'Refresh token is required'}, status=status.HTTP_400_BAD_REQUEST)


class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter
    callback_url = "http://localhost:3000/"
    client_class = OAuth2Client
