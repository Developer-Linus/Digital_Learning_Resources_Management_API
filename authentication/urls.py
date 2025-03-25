from django.urls import path
from allauth.account.views import (
    SignupView,
    LoginView,
    LogoutView,
    PasswordChangeView,
    PasswordResetView,
    PasswordResetDoneView,
    ConfirmEmailView,
)

from django.contrib.auth.views import (
    PasswordResetConfirmView,
    PasswordResetCompleteView,
)

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView



from allauth.socialaccount.views import signup
from authentication.views import GoogleLogin



urlpatterns = [
    # Registration
    path('register/', SignupView.as_view(), name='account_signup'),
    path('api/auth/confirm-email/', ConfirmEmailView.as_view(), name='account_email_verification_sent'),
    path('api/auth/confirm-email/<key>/', ConfirmEmailView.as_view(), name='account_confirm_email'),
    
    # Login
    path("login/", LoginView.as_view(), name="account_login"),
    
    #Logout
    path('logout/', LogoutView.as_view(), name='logout'),
    
    # Password management
    path('api/auth/password/change/', PasswordChangeView.as_view(), name='account_change_password'),
    path('api/auth/password/reset/', PasswordResetView.as_view(), name='account_reset_password'),
    path('api/auth/password/reset/done/', PasswordResetDoneView.as_view(), name='account_reset_password_done'),
    path('api/auth/reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='account_reset_password_confirm'),
    path('api/auth/reset/done/', PasswordResetCompleteView.as_view(), name='account_reset_password_complete'), 
    
    # URLs for Google Oauth login
    path("signup/", signup, name="socialaccount_signup"),
    path("google/", GoogleLogin.as_view(), name="google_login"),
]