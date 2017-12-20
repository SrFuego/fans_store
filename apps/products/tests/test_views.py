# Python imports


# Django imports


# Third party apps imports
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase


# Local imports


# Create your view tests here.
class MostViewedTests(APITestCase):
    def setUp(self):
        self.most_visits_url = reverse("most-viewed")

    def test_get_response(self):
        response = self.client.get(self.most_visits_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # def tearDown(self):


class NewersTests(APITestCase):
    def setUp(self):
        self.newers_url = reverse("newers")

    def test_get_response(self):
        response = self.client.get(self.newers_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # def tearDown(self):
