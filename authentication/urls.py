from django.urls import path
from .views import UserRegistrationView, LoginView

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from allauth.account.views import confirm_email

from allauth.socialaccount.views import signup
from authentication.views import GoogleLogin



urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path("login/", LoginView.as_view(), name="login"),
    # path("logout/", LogoutView.as_view(), name="logout"),
    
    #URLs for obtaining tokens
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'), 
    
    # URLs for Google Oauth login
    path("signup/", signup, name="socialaccount_signup"),
    path("google/", GoogleLogin.as_view(), name="google_login"),
]