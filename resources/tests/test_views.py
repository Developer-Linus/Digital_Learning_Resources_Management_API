import json
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from resources.models import Category, Resource, LearningLog, ResourceStatus, Bookmark

User = get_user_model()

class CategoryViewTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(email='testuser@mail.com', password='testpassword')
        self.category = Category.objects.create(owner=self.user, name='test category', description='test description')
        self.client.force_authenticate(user=self.user)
    def test_category_list_view(self):
        response = self.client.get(reverse('list_categories'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['data']), 1)
    def test_category_create_view(self):
        data = {'name': 'another category', 'description': 'another description'}
        response = self.client.post(reverse('create_category'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Category.objects.count(), 2)
    def test_category_delete_view(self):
        response = self.client.delete(reverse('delete_category', args=[self.category.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Category.objects.count(), 0)
class ResourceViewTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(email='testuser@mail.com', password='password123')
        self.category = Category.objects.create(owner=self.user, name='Test Category', description='Test Description')
        self.resource = Resource.objects.create(owner=self.user, category=self.category, resource_name='Test Resource', resource_author='Test Author', resource_url='https://www.example.com', publication_date='2022-01-01')
        self.client.force_authenticate(user=self.user)
    def test_resource_list_view(self):
        response = self.client.get(reverse('list_resources'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['data']), 1)

    def test_resource_create_view(self):
        data = {'category': self.category.id,'resource_name': 'New Resource','resource_author': 'New Author','resource_url': 'https://www.example.com', 'publication_date': '2022-01-01'}
        response = self.client.post(reverse('create_resource'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Resource.objects.count(), 2)
    def test_resource_detail_view(self):
        response = self.client.get(reverse('resource', args=[self.resource.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['data']['id'], self.resource.id)
    def test_resource_update_view(self):
        data = {'category': self.category.id,'resource_name': 'Updated Resource','resource_author': 'Updated Author','resource_url': 'https://www.example.com', 'publication_date': '2022-01-01'}
        response = self.client.put(reverse('update_resource', args=[self.resource.id]), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Resource.objects.get(id=self.resource.id).resource_name, 'Updated Resource')
    def test_resource_delete_view(self):
        response = self.client.delete(reverse('delete_resource', args=[self.resource.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Resource.objects.count(), 0)
class LearningLogViewTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(email='testuser@mail.com', password='password123')
        self.category = Category.objects.create(owner=self.user, name='Test Category', description='Test Description')
        self.resource = Resource.objects.create(owner=self.user, category=self.category, resource_name='Test Resource', resource_author='Test Author', resource_url='https://www.example.com', publication_date='2022-01-01')
        self.learning_log = LearningLog.objects.create(owner=self.user, resource=self.resource, notes='Test Notes', review='Test Review')
        self.client.force_authenticate(user=self.user)

    def test_learning_log_list_view(self):
        response = self.client.get(reverse('list_learning_logs'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['data']), 1)

    def test_learning_log_create_view(self):
        new_resource = Resource.objects.create(owner=self.user, category=self.category, resource_name='New Resource', resource_author='New Author', resource_url='https://new-resource.com', publication_date='2022-01-01')
        data = {'resource': new_resource.id, 'notes': 'New Notes','review': 'New Review'}
        response = self.client.post(reverse('create_learning_log'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(LearningLog.objects.count(), 2)

    def test_learning_log_detail_view(self):
        response = self.client.get(reverse('learning_log', args=[self.learning_log.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['data']['id'], self.learning_log.id)

    def test_learning_log_update_view(self):
        data = {'resource': self.resource.id, 'notes': 'Updated Notes','review': 'Updated Review'}
        response = self.client.put(reverse('update_learning_log', args=[self.learning_log.id]), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(LearningLog.objects.get(id=self.learning_log.id).notes, 'Updated Notes')

    def test_learning_log_delete_view(self):
        response = self.client.delete(reverse('delete_learning_log', args=[self.learning_log.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(LearningLog.objects.count(), 0)


class ResourceStatusViewTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(email='testuser@mail.com', password='password123')
        self.category = Category.objects.create(owner=self.user, name='Test Category', description='Test Description')
        self.resource = Resource.objects.create(owner=self.user, category=self.category, resource_name='Test Resource', resource_author='Test Author', resource_url='https://www.example.com', publication_date='2022-01-01')
        self.resource_status = ResourceStatus.objects.create(owner=self.user, resource=self.resource, in_progress=True, is_completed=False)
        self.client.force_authenticate(user=self.user)

    def test_resource_status_list_view(self):
        response = self.client.get(reverse('list_resources_status'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['data']), 1)

    def test_resource_status_create_view(self):
        new_resource = Resource.objects.create(owner=self.user, category=self.category, resource_name='another Resource', resource_author='NAuthor', resource_url='https://another-resource.com', publication_date='2022-01-01')
        data = {'resource': new_resource.id, 'in_progress': True, 'is_completed': False}
        response = self.client.post(reverse('create_resource_status'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(ResourceStatus.objects.count(), 2)

    def test_resource_status_detail_view(self):
        response = self.client.get(reverse('resource_status', args=[self.resource_status.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['data']['id'], self.resource_status.id)

    def test_resource_status_update_view(self):
        data = {'resource': self.resource.id, 'in_progress': False, 'is_completed': True}
        response = self.client.put(reverse('update_resource_status', args=[self.resource_status.id]), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(ResourceStatus.objects.get(id=self.resource_status.id).in_progress, False)

    def test_resource_status_delete_view(self):
        response = self.client.delete(reverse('delete_resource_status', args=[self.resource_status.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(ResourceStatus.objects.count(), 0)


class BookmarkViewTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(email='testuser@mail.com', password='password123')
        self.category = Category.objects.create(owner=self.user, name='Test Category', description='Test Description')
        self.resource = Resource.objects.create(owner=self.user, category=self.category, resource_name='Test Resource', resource_author='Test Author', resource_url='https://www.example.com', publication_date='2022-01-01')
        self.bookmark = Bookmark.objects.create(owner=self.user, resource=self.resource)
        self.client.force_authenticate(user=self.user)

    def test_bookmark_list_view(self):
        response = self.client.get(reverse('bookmarks'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['data']), 1)

    def test_bookmark_create_view(self):
        new_resource = Resource.objects.create(owner=self.user, category=self.category, resource_name='New Resource', resource_author='New Author', resource_url='https://new-resource.com', publication_date='2022-01-01')
        data = {'resource': new_resource.id}
        response = self.client.post(reverse('create_bookmark'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Bookmark.objects.count(), 2)

    def test_bookmark_detail_view(self):
        response = self.client.get(reverse('bookmark', args=[self.bookmark.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['data']['id'], self.bookmark.id)

    def test_bookmark_delete_view(self):
        response = self.client.delete(reverse('delete_bookmark', args=[self.bookmark.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Bookmark.objects.count(), 0)
        
        

    
    