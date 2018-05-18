# Python imports


# Django imports
from django.urls import reverse


# Third party apps imports
from rest_framework import status
from rest_framework.test import APITestCase


# Local imports


# Create your viewset tests here.
class OrderTestCase(APITestCase):
    def setUp(self):
        self.orders_url = reverse("api_v1:orders-list")

    def test_get_response(self):
        response = self.client.get(self.orders_url)
        self.assertEqual(
            response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_create_order(self):
        data = {
            "name": "Manuel Jesus De la Cruz Sotelo",
            "phone": "991738271",
            "size": "L",
        }
        response = self.client.post(self.orders_url, data=data)
        self.assertEqual(
            response.status_code, status.HTTP_201_CREATED)

    # def tearDown(self):
    #     for order in self.orders:
    #         order.delete()
