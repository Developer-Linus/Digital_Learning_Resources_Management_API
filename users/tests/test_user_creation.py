from django.test import TestCase
from django.contrib.auth import get_user_model
from users.models import Profile
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


'''
TESTS FOR USER CREATION
'''


class UserProfileSignalTests(TestCase):
    
    def setUp(self):
        self.User = get_user_model()
        self.user = self.User.objects.create_user(email='testemail@mail.com', password='testpassword')
        self.admin = self.User.objects.create_superuser(email='admin@mail.com', password='adminpass')
    
    def test_user_creation(self):
        #Test if a normal user is successfully created
        self.assertEqual(self.user.email, 'testemail@mail.com')
    
    def test_admin_creation(self):
        #Test if an admin is successfully created
        self.assertEqual(self.admin.email, 'admin@mail.com')
    
    def test_user_must_have_role(self):
        # Check that user must have role during registration
        with self.assertRaises(Exception):
            self.user = self.User.create_user(email='norole@mail.com', password='norolepass', role=None)
        
    def test_profile_created_with_user(self):
        # Check if a profile is automatically created when a user registers
        profile_exists = Profile.objects.filter(user=self.user).exists()
        self.assertTrue(profile_exists, 'Profile was not created automatically.')
        
    def test_profile_persists_after_user_update(self):
        self.user.first_name = 'First'
        self.user.save()
        profile_exists = Profile.objects.filter(user=self.user).exists()
        self.assertTrue(profile_exists, 'Profile was removed after user update.')
    
    def test_profile_deleted_with_user(self):
        user_id = self.user.id
        self.user.delete()
        profile_exists = Profile.objects.filter(user_id=user_id).exists()
        self.assertFalse(profile_exists, 'Profile was not removed with user.')
    
    def test_cannot_create_user_with_invalid_email(self):
        with self.assertRaises(ValueError):
            self.User.objects.create_user(email='not-email', password='passtest')

    def test_cannot_create_user_with_duplicate_email(self):
        # Tests to check no new user is created with existing email address
        with self.assertRaises(Exception):
            self.user = self.User.objects.create(email=self.user.email, password='newpass')
    
    def test_no_profile_for_superusers(self):
        #Test for no profile should be created for superusers
        self.admin_user = self.User.objects.create_superuser(email='admin2@mail.com', password='admin1testpass2')
        profile_exists = Profile.objects.filter(user=self.admin_user).exists()
        self.assertFalse(profile_exists, 'Profile for superusers must not exist.')