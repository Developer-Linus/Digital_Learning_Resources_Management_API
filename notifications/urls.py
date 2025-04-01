from django.urls import path
from .views import NotificationListAPIView, MarkNotificationAsReadView


urlpatterns = [
    path('api/notifications/', NotificationListAPIView.as_view(), name='notifications'),
    path('api/notifications/<int:pk>/mark_as_read/', MarkNotificationAsReadView.as_view(), name='mark_notification_as_read'),
]