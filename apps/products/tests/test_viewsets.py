# Python imports


# Django imports
from django.urls import reverse


# Third party apps imports
from rest_framework import status
from rest_framework.test import APITestCase


# Local imports


# Create your viewset tests here.
class KindTests(APITestCase):
    def setUp(self):
        self.visits_url = reverse("api:kind-list")

    def test_get_kind_list(self):
        response = self.client.get(self.visits_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # def tearDown(self):
