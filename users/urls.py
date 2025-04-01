from django.urls import path
from.views import ProfileDetailAPIView, ProfileUpdateAPIView, ProfileDeleteAPIView

urlpatterns = [
    path('profile/', ProfileDetailAPIView.as_view(), name='detail_profile'),
    path('profile/<int:pk>/update/', ProfileUpdateAPIView.as_view(), name='update_profile'),
    path('profile/<int:pk>/delete/', ProfileDeleteAPIView.as_view(), name='delete_profile'),
]