from django.urls import path
from.views import ProfileDetailAPIView, ProfileUpdateAPIView, ProfileDeleteAPIView

urlpatterns = [
    path('profile/', ProfileDetailAPIView.as_view(), name='profile_detail'),
    path('profile/update/', ProfileUpdateAPIView.as_view(), name='profile_update'),
    path('profile/delete/', ProfileDeleteAPIView.as_view(), name='profile_delete'),
]