from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token

from .models import Category, Task, Comment

User = get_user_model()


class TaskModelTest(TestCase):
    """    Тест модели Task    """

    # Инит начальных данных для теста
    def setUp(self):
        self.user = User.objects.create_user(email='user@mail.ru', password='123456')
        self.category = Category.objects.create(name='Work', color='RED')
        self.task = Task.objects.create(
            title='Test Task',
            description='Test Description',
            category=self.category,
            status='DRAFT',
            owner=self.user,
            tags='test,task',
            is_active=True
        )

    # Проверяем создание задачи
    def test_create_task(self):
        task = Task.objects.create(
            title='Second Task',
            description='Another Description',
            category=self.category,
            status='DRAFT',
            owner=self.user,
            tags='another,task',
            is_active=True
        )
        self.assertEqual(Task.objects.count(), 2)
        self.assertEqual(task.title, 'Second Task')

    # Обновляем задачу и проверяем, что изменения занесены.
    def test_update_task(self):
        self.task.title = 'Updated Task'
        self.task.save()
        self.task.refresh_from_db()
        self.assertEqual(self.task.title, 'Updated Task')

    # Удаляем задачу и проверяем, что ее больше нет
    def test_delete_task(self):
        self.task.delete()
        self.assertEqual(Task.objects.count(), 0)

    # Проверяем получения задачи
    def test_retrieve_task(self):
        task = Task.objects.get(id=self.task.id)
        self.assertEqual(task.title, 'Test Task')


class CategoryModelTest(TestCase):
    """    Тест модели Category    """

    def setUp(self):
        self.category = Category.objects.create(name='Home', color='GREEN')

    def test_create_category(self):
        category = Category.objects.create(name='Leisure', color='BLUE')
        self.assertEqual(Category.objects.count(), 2)
        self.assertEqual(category.name, 'Leisure')

    def test_update_category(self):
        self.category.name = 'Updated Home'
        self.category.save()
        self.category.refresh_from_db()
        self.assertEqual(self.category.name, 'Updated Home')

    def test_delete_category(self):
        self.category.delete()
        self.assertEqual(Category.objects.count(), 0)

    def test_retrieve_category(self):
        category = Category.objects.get(id=self.category.id)
        self.assertEqual(category.name, 'Home')


class CommentIntegrationTest(TestCase):
    """    Тест на создание комметов в Task    """

    def setUp(self):
        self.user = User.objects.create_user(email='user@mail.ru', password='12345')
        self.category = Category.objects.create(name='Work', color='RED')
        self.task = Task.objects.create(
            title='Test Add Comments',
            description='Task Description',
            category=self.category,
            status='DRAFT',
            owner=self.user,
            tags='test,task',
            is_active=True
        )

    def test_add_and_retrieve_comments(self):
        comment1 = Comment.objects.create(task=self.task, comment='First comment')
        comment2 = Comment.objects.create(task=self.task, comment='Second comment')

        comments = self.task.comments.all()
        self.assertEqual(comments.count(), 2)
        self.assertIn(comment1, comments)
        self.assertIn(comment2, comments)
        self.assertEqual(comments[0].comment, 'First comment')
        self.assertEqual(comments[1].comment, 'Second comment')
