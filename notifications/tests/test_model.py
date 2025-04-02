from django.test import TestCase
from django.contrib.auth import get_user_model
from notifications.models import Notification
from resources.models import Resource, Category

User = get_user_model()

class NotificationModelTestCase(TestCase):
    def setUp(self):
        # Create a user
        self.user = User.objects.create_user(email='testuser@mail.com', password='password123')
        self.category = Category.objects.create(owner=self.user, name='test category', description='test description')
        # Create a resource
        self.resource = Resource.objects.create(owner=self.user, category=self.category, resource_name='Test Resource', resource_author='Test Author', resource_url='https://test-resource.com', publication_date='2022-01-01')

    def test_notification_creation(self):
        # Create a notification
        notification = Notification.objects.create(
            recipient=self.user,
            actor=self.user,
            verb='added',
            target=self.resource
        )
        
        # Check if notification is created successfully
        self.assertIsNotNone(notification)
        self.assertEqual(notification.recipient, self.user)
        self.assertEqual(notification.actor, self.user)
        self.assertEqual(notification.verb, 'added')
        self.assertEqual(notification.target, self.resource)

    def test_notification_string_representation(self):
        # Create a notification
        notification = Notification.objects.create(
            recipient=self.user,
            actor=self.user,
            verb='added',
            target=self.resource
        )
        
        # Check if string representation is correct
        self.assertEqual(str(notification), f'{self.user} added {self.resource}')