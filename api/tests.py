# from django.test import TestCase
from meetups.models import Location
from rest_framework.test import APIClient
from rest_framework.test import APITestCase
from rest_framework import status

class ApiTestCase(APITestCase):

    """
    Test suite for API
    """
    def setUp(self):
        self.client = APIClient()
        self.data = {
            "name": "Party House",
            "address": "Looe"
        }
        self.url = "/api/locations/"

    def test_create_location(self):
        '''
        test LocationViewSet create method
        
        This is an example test, it's not really necessary here
        as this endpoint is not a custom implementation
        '''
        data = self.data
        response = self.client.post(self.url, data)
        print(response.status_code)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Location.objects.count(), 1)
        self.assertEqual(Location.objects.get().name, "Party House")