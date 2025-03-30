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
    
    # LearningLogs URLs
    path('api/learning_logs/', views.LearningLogListAPIView.as_view(), name='list_learning_logs'),
    path('api/learning_logs/<int:pk>/retrieve/', views.LearningLogDetailAPIView.as_view(), name='learning_log'),
    path('api/learning_logs/<int:pk>/update/', views.LearningLogUpdateAPIView.as_view(), name='update_learning_log'),
    path('api/learning_logs/create/', views.LearningLogCreateAPIView.as_view(), name='create_learning_log'),
    path('api/learning_logs/<int:pk>/delete/', views.LearningLogDeleteAPIView.as_view(), name='delete_learning_log'),
]