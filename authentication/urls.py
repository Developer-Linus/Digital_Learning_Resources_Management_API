from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import RegisterView, LoginAPIView, LogoutAPIView, VerifyEmail


urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/auth/register/', RegisterView.as_view(), name='register'),
    path('api/auth/confirm-email/', VerifyEmail.as_view(), name='confirm_email'),
    path('api/auth/login/', LoginAPIView.as_view(), name='login'),
    path('api/auth/logout/', LogoutAPIView.as_view(), name='logout'),
]