import datetime
from django.test import TestCase
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
from resources.models import Category, Resource, LearningLog, ResourceStatus, Bookmark
from django.db import IntegrityError

User = get_user_model()

class TestCategoryModel(TestCase):
    # Test cases for the category model
    def setUp(self):
        self.user = User.objects.create_user(email='testuser@mail.com', password='testpassword')
    def test_category_creation(self):
        # Test for creating a new category
        category = Category.objects.create(owner=self.user, name='test category')
        self.assertEqual(category.owner, self.user)
        self.assertEqual(category.name, 'test category')
    def test_category_string_representation(self):
        category = Category.objects.create(owner=self.user, name='test category')
        self.assertEqual(str(category), 'test category')
    def test_category_detault_name(self):
        category = Category.objects.create(owner=self.user)
        self.assertEqual(category.name, 'Uncategorized')
    def test_category_name_uniqueness(self):
        category = Category.objects.create(owner=self.user, name='test category')
        with self.assertRaises(IntegrityError):
            category = Category.objects.create(owner=self.user, name='test category')
class TestResourceModel(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(email='testuser@mail.com', password='testpassword')
        self.category = Category.objects.create(owner=self.user, name='test category')
    def test_resource_creation(self):
        resource = Resource.objects.create(
            owner=self.user,
            category=self.category,
            resource_name='test resource',
            resource_author='test author',
            resource_url='https://example.com',
            publication_date=datetime.date.today()
        )
        self.assertEqual(resource.owner, self.user)
        self.assertEqual(resource.category, self.category)
        self.assertEqual(resource.resource_name, 'test resource')
        self.assertEqual(resource.resource_author, 'test author')
        self.assertEqual(resource.resource_url, 'https://example.com')
        self.assertEqual(resource.publication_date, datetime.date.today())
    def test_resource_string_representation(self):
        resource = Resource.objects.create(
            owner=self.user,
            category=self.category,
            resource_name='test resource',
            resource_author='test author',
            resource_url='https://example.com',
            publication_date=datetime.date.today()
        )
        self.assertEqual(str(resource), f'test resource by test author')
        
class TestLearningLogModel(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(email='testuser@mail.com', password='password123')
        self.category = Category.objects.create(owner=self.user, name='Test Category')
        self.resource = Resource.objects.create(
            owner=self.user, 
            category=self.category, 
            resource_name='Test Resource', 
            resource_author='Test Author', 
            resource_url='https://www.example.com', 
            publication_date=datetime.date.today()
        )
    def test_learning_log_creation(self):
        learninglog = LearningLog.objects.create(
            owner=self.user,
            resource=self.resource,
            notes= 'Test notes',
            review = 'Test review'
        )
        self.assertEqual(learninglog.owner, self.user)
        self.assertEqual(learninglog.resource, self.resource)
        self.assertEqual(learninglog.notes, 'Test notes')
        self.assertEqual(learninglog.review, 'Test review')
    def test_learning_log_string_representation(self):
        learninglog = LearningLog.objects.create(
            owner=self.user,
            resource=self.resource,
            notes= 'Test notes',
            review = 'Test review.'
        )
        self.assertEqual(str(learninglog), f'Notes for Test Resource are Test notes...')

class TestResourceStatusModel(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(email='testuser@mail.com', password='password123')
        self.category = Category.objects.create(owner=self.user, name='Test Category')
        self.resource = Resource.objects.create(
            owner=self.user, 
            category=self.category, 
            resource_name='Test Resource', 
            resource_author='Test Author', 
            resource_url='https://www.example.com', 
            publication_date=datetime.date.today()
        )
    def test_resource_status_creation(self):
        resource_status = ResourceStatus.objects.create(
            owner=self.user, 
            resource=self.resource
        )
        self.assertEqual(resource_status.owner, self.user)
        self.assertEqual(resource_status.resource, self.resource)
        self.assertFalse(resource_status.is_completed)
        self.assertFalse(resource_status.in_progress)
        self.assertFalse(resource_status.is_important)

class TestBoomarkModel(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(email='testuser@mail.com', password='password123')
        self.category = Category.objects.create(owner=self.user, name='Test Category')
        self.resource = Resource.objects.create(
            owner=self.user, 
            category=self.category, 
            resource_name='Test Resource', 
            resource_author='Test Author', 
            resource_url='https://www.example.com', 
            publication_date=datetime.date.today()
        )
    def test_bookmark_creation(self):
        bookmark = Bookmark.objects.create(
            owner=self.user, 
            resource=self.resource
        )
        self.assertEqual(bookmark.owner, self.user)
        self.assertEqual(bookmark.resource, self.resource)
    