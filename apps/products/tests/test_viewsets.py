# Python imports


# Django imports
from django.urls import reverse


# Third party apps imports
from model_mommy import mommy
from rest_framework import status
from rest_framework.test import APITestCase


# Local imports
from ..models import Product


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
        self.products = mommy.make(Product, _quantity=6)

    def test_get_response(self):
        response = self.client.get(self.most_visits_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_6_elements(self):
        response = self.client.get(self.most_visits_url)
        self.assertEqual(len(response.data), Product.objects.all().count())

    def tearDown(self):
        for product in self.products:
            product.delete()


class NewersTests(APITestCase):
    def setUp(self):
        self.newers_url = reverse("api_v1:newers-list")
        self.products = mommy.make(Product, _quantity=6)

    def test_get_response(self):
        response = self.client.get(self.newers_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_6_elements(self):
        response = self.client.get(self.newers_url)
        self.assertEqual(len(response.data), Product.objects.all().count())

    def tearDown(self):
        for product in self.products:
            product.delete()
