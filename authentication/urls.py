from django.urls import path
from .views import UserRegistrationView, LoginView, LogoutView
from allauth.account import views as allauth_account_views

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from allauth.account.views import confirm_email

from allauth.socialaccount.views import signup
from authentication.views import GoogleLogin



urlpatterns = [
    # Registration
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('api/auth/confirm-email/', allauth_account_views.ConfirmEmailView.as_view(), name='account_email_verification_sent'),
    path('api/auth/confirm-email/<key>/', allauth_account_views.ConfirmEmailView.as_view(), name='account_confirm_email'),
    
    # Login
    path("login/", LoginView.as_view(), name="login"),
    
    #Logout
    path('logout/', LogoutView.as_view(), name='logout'),
    
    # Password management
    # path('api/auth/password/change/', allauth_account_views.PasswordChangeView.as_view(), name='account_change_password'),
    # path('api/auth/password/reset/', allauth_account_views.PasswordResetView.as_view(), name='account_reset_password'),
    # path('api/auth/password/reset/done/', allauth_account_views.PasswordResetDoneView.as_view(), name='account_reset_password_done'),
    # path('api/auth/reset/<uidb64>/<token>/', allauth_account_views.PasswordResetConfirmView.as_view(), name='account_reset_password_confirm'),
    # path('api/auth/reset/done/', allauth_account_views.PasswordResetCompleteView.as_view(), name='account_reset_password_complete'), 
    
    # URLs for Google Oauth login
    path("signup/", signup, name="socialaccount_signup"),
    path("google/", GoogleLogin.as_view(), name="google_login"),
]