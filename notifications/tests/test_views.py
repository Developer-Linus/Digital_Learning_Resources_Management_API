from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from notifications.models import Notification
from resources.models import Resource, Category

User = get_user_model()

class NotificationViewTestCase(APITestCase):
    def setUp(self):
        # Create a user
        self.user = User.objects.create_user(email='testuser@mail.com', password='password123')
        self.category = Category.objects.create(owner=self.user, name='test category', description='test description')
        # Create a resource
        self.resource = Resource.objects.create(owner=self.user, category=self.category, resource_name='Test Resource', resource_author='Test Author', resource_url='https://test-resource.com', publication_date='2022-01-01')
        
        # Create a notification
        self.notification = Notification.objects.create(
            recipient=self.user,
            actor=self.user,
            verb='added',
            target=self.resource
        )
        
        # Authenticate the client
        self.client.force_authenticate(user=self.user)

    def test_notification_list_view(self):
        # Get the notification list view
        response = self.client.get(reverse('notifications'))
        
        # Check if the view returns a 200 status code
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # Check if the notification is in the response
        self.assertIn(self.notification.id, [n['id'] for n in response.data])

    def test_mark_notification_as_read_view(self):
        # Mark the notification as read
        response = self.client.patch(reverse('mark_notification_as_read', args=[self.notification.id]), {'read': True})
        
        # Check if the view returns a 200 status code
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # Check if the notification is marked as read
        self.notification.refresh_from_db()
        self.assertTrue(self.notification.read)