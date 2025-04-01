from rest_framework import status, permissions, generics, views
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserRegistrationSerializer, LoginSerializer, LogoutSerializer, EmailVerificationSerializer
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model
from .utils import Util
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
import jwt
from django.conf import settings
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

User = get_user_model()

# Define a class-based view for handling user registration
class RegisterView(generics.GenericAPIView):
    serializer_class = UserRegistrationSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)
        if serializer.is_valid():
            user = serializer.save()
            user_data = serializer.data

            # Get the user instance from the database using the email address
            user = User.objects.get(email=user_data['email'])

            # Generate a refresh token for the user
            token = RefreshToken.for_user(user).access_token

            # Get the current site domain
            current_site = get_current_site(request).domain
            # Get the relative URL for email verification
            relativeLink = reverse('confirm_email')
            # Construct the absolute URL for email verification
            absurl = 'http://' + current_site + relativeLink + '?token=' + str(token)

            # Create the email body with the verification link
            email_body = 'Hi,' + user.email +'Use the link below to verify your email\n' + absurl
            # Create a dictionary with email data
            data = {'email_body': email_body, 'to_email': user.email, 'email_subject': 'Verify Your Email'}

            # Send the email using the Util class
            Util.send_email(data)

            # Return a success response with a message
            return Response({'message': 'User registered successfully. Check your email for verification link.'}, status=status.HTTP_201_CREATED)
        # If the serializer is not valid, return an error response with the error details
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Define a class for handling email verification
class VerifyEmail(views.APIView):
    serializer_class = EmailVerificationSerializer
    
    token_param_config = openapi.Parameter('token', in_=openapi.IN_QUERY, type=openapi.TYPE_STRING)
    
    @swagger_auto_schema(manual_parameters=[token_param_config])
    def get(self, request):
        # Get the token from the request query parameters
        token = request.GET.get('token')

        # Decode the token and verify the user's email
        try:
            # Decode the token using the secret key and HS256 algorithm
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
            # Get the user instance from the database using the user ID from the token payload
            user = User.objects.get(id=payload['user_id'])

            # Check if the user's email is not verified
            if not user.is_verified:
                # Mark the user's email as verified
                user.is_verified = True
                user.save()
                return Response({'message': 'Email verified successfully'}, status=status.HTTP_200_OK)
            else:
                # If the user's email is already verified, return an error response with a message
                return Response({'message': 'Email already verified'}, status=status.HTTP_400_BAD_REQUEST)
        # Catch the exception if the token has expired
        except jwt.ExpiredSignatureError:
            return Response({'error': 'The token has expired.'}, status=status.HTTP_400_BAD_REQUEST)
        # Catch the exception if the token is invalid
        except jwt.DecodeError:
            # Return an error response with a message
            return Response({'error': 'Invalid token.'}, status=status.HTTP_400_BAD_REQUEST)
        # Catch the exception if the user does not exist
        except User.DoesNotExist:
            return Response({'error': 'User does not exist'}, status=status.HTTP_404_NOT_FOUND)
        # Catch any other exceptions
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
# Define class-based view for login
class LoginAPIView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

# Define class-based view for logout     
class LogoutAPIView(generics.GenericAPIView):
    serializer_class = LogoutSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response({'Message': 'Logout successful.'}, status=status.HTTP_200_OK)
    
    