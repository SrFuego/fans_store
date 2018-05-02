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
class MostViewedTests(APITestCase):
    def setUp(self):
        self.most_visits_url = reverse("api_v1:most_viewed-list")
        self.products = mommy.make(Product, _quantity=10)

    def test_get_response(self):
        response = self.client.get(self.most_visits_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_6_elements(self):
        response = self.client.get(self.most_visits_url)
        self.assertEqual(len(response.data), 6)

    def tearDown(self):
        for product in self.products:
            product.delete()


class NewersTests(APITestCase):
    def setUp(self):
        self.newers_url = reverse("api_v1:newers-list")
        self.products = mommy.make(Product, _quantity=10)

    def test_get_response(self):
        response = self.client.get(self.newers_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_6_elements(self):
        response = self.client.get(self.newers_url)
        self.assertEqual(len(response.data), 6)

    def tearDown(self):
        for product in self.products:
            product.delete()


class ProductTests(APITestCase):
    def setUp(self):
        self.product = mommy.make(Product)
        self.product_url = reverse(
            "api_v1:products-detail", args=[self.product.id])

    def test_get_response(self):
        response = self.client.get(self.product_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_increase_views(self):
        views_before = self.product.views
        response_1 = self.client.get(self.product_url)
        views_after_1 = Product.objects.get(id=self.product.id).views
        response_2 = self.client.get(self.product_url)
        views_after_2 = Product.objects.get(id=self.product.id).views
        self.assertEqual(response_1.status_code, status.HTTP_200_OK)
        self.assertGreater(views_after_1, views_before)
        self.assertEqual(response_2.status_code, status.HTTP_200_OK)
        self.assertGreater(views_after_2, views_before)
        self.assertGreater(views_after_2, views_after_1)

    def tearDown(self):
        self.product.delete()
