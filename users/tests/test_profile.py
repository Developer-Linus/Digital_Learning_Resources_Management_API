from django.contrib.auth import get_user_model
from users.models import Profile
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

'''
TESTS FOR RETRIEVING, UPDATING, AND DELETING PROFILE
'''
class ProfileAPITestCase(APITestCase):
    # This method is called every time before any test to set testing environment
    def setUp(self):
        # Define custom user
        self.User = get_user_model()
        # Create a new user
        self.user = self.User.objects.create_user(username='testuser', email='testuser@mail.com', password='testpassword')
        # Create a new profile if none exists or retrieve if it exists
        self.profile, created = Profile.objects.get_or_create(user=self.user)
        # Authenticate the user
        self.client.force_authenticate(user=self.user)
        
    # This method is called every time after any test to clean up
    def tearDown(self):
        # Delete the user and profile
        self.user.delete()
        self.profile.delete()

    # Test to view user's profile
    def test_view_profile(self):
        url = reverse('view_profile')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['user']['id'], str(self.user.id))
    # Test to update user's profile
    def test_update_profile(self):
        url = reverse('update_profile', kwargs={'id': self.user.id})
        # Dictionary with updated profile data
        data = {
            'first_name': 'Peter',
            'last_name': 'Johns',
        }
        # Make a PUT request to the update endpoint with updated data
        response = self.client.put(url, data, format='json')
        # Check if the response status is 200(OK)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        #Check if the response contains the updated profile data
        updated_user = self.User.objects.get(email=self.user.email)
        self.assertEqual(updated_user.profile.first_name, 'Peter')
        self.assertEqual(updated_user.profile.last_name, 'Johns')
        
    # Test to delete user's profile
    def test_delete_profile(self):
        url = reverse('delete_profile', kwargs={'id': self.user.id})
        response = self.client.delete(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {'message' : 'Profile successfully deleted'})
        
        # Test to view user's profile without authentication
    def test_unauthenticated_user(self):
        self.client.force_authenticate(user=None)
        url = reverse('view_profile')
        response = self.client.get(url)
            
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
    # Test to update user's profile with invalid data
    def test_update_profile_with_invalid_data(self):
        
        data = {
            'first_name' : 'John'*1000,
        }
        
        url = reverse('update_profile', kwargs={'id': self.user.id})
        response = self.client.put(url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)