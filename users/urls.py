from django.urls import path
from.views import ProfileView, UpdateProfileView, DeleteProfileView

urlpatterns = [
    path('user-profile/', ProfileView.as_view(), name='view_profile'),
    path('user-profile/update/', UpdateProfileView.as_view(), name='update_profile'),
    path('user-profile/delete/', DeleteProfileView.as_view(), name='delete_profile'),
]