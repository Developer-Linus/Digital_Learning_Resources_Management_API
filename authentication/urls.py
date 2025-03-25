from django.urls import path
from .views import RegisterView, LoginView


urlpatterns = [
    path('api/auth/register/', RegisterView.as_view(), name='register'),
    path('api/auth/login/', LoginView.as_view(), name='login'),
]