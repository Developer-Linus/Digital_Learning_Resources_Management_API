from rest_framework import generics, permissions, filters
from.models import Notification
from rest_framework.pagination import PageNumberPagination
from .serializers import NotificationSerializer
from rest_framework.response import Response

# View for fetching notifications related to logged-in user
class NotificationListAPIView(generics.ListAPIView):
    
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['verb', 'target']
    ordering_fields = ['verb', 'target', 'timestamp']
    pagination_class = PageNumberPagination
    page_size = 10
    
    def get_queryset(self):
        return Notification.objects.filter(recipient=self.request.user)

# View for marking a notification as read
class MarkNotificationAsReadView(generics.UpdateAPIView):
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Notification.objects.filter(recipient=self.request.user)

    def partial_update(self, request, *args, **kwargs):
        notification = self.get_object()
        serializer = self.get_serializer(notification, data={'read': True}, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {'message': 'Notification marked as read'},
            status=200
        )
    
