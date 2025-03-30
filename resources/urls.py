from django.urls import path
from . import views


urlpatterns = [
    # Categories URLs
    path('api/categories/', views.CategoryListAPIView.as_view(), name='list_categories'),
    path('api/categories/create/', views.CategoryCreateAPIView.as_view(), name='create_category'),
    path('api/categories/<int:pk>/delete/', views.CategoryDeleteAPIView.as_view(), name='delete_category'),
    
    # Resources URLs
    path('api/resources/', views.ResourceListAPIView.as_view(), name='list_resources'),
    path('api/resources/<int:pk>/retrieve/', views.ResourceDetailAPIView.as_view(), name='resource'),
    path('api/resources/<int:pk>/update/', views.ResourceUpdateAPIView.as_view(), name='update_resource'),
    path('api/resources/create/', views.ResourceCreateAPIView.as_view(), name='create_resource'),
    path('api/resources/<int:pk>/delete/', views.ResourceDeleteAPIView.as_view(), name='delete_resource'),
    
]