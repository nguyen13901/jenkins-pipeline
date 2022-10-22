from rest_framework import status
from rest_framework.test import APITestCase, APIClient

class CategoryTests(APITestCase):
  client = APIClient()

  def test_create_create(self):
    pass