import json

from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token

from .models import Category


# class RegistrationTestCase(APITestCase):
#
#     def test_registration(self):
#         data = {
#               "email": "user@example.com",
#               "password": "string",
#               "first_name": "string1",
#               "last_name": "string2"
#         }
#         response = self.client.post("api/register/", data)
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class CategoryModelTests(TestCase):
    """    Тест модели категории    """

    def setUp(self):
        self.category = Category(
            name='First',
            color='WHITE',
        )

    def test_create_category(self):
        self.assertIsInstance(self.category, Category)

    def test_str_representation(self):
        self.assertEqual(str(self.category), "First")
