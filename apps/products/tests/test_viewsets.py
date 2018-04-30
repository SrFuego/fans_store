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
        self.visits_url = reverse("api_v1:kinds-list")

    def test_get_kind_list(self):
        response = self.client.get(self.visits_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # def tearDown(self):


class MostViewedTests(APITestCase):
    def setUp(self):
        self.most_visits_url = reverse("api_v1:most_viewed-list")

    def test_get_response(self):
        response = self.client.get(self.most_visits_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # def tearDown(self):


class NewersTests(APITestCase):
    def setUp(self):
        self.newers_url = reverse("api_v1:newers-list")

    def test_get_response(self):
        response = self.client.get(self.newers_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # def tearDown(self):
