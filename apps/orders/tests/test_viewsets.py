# Python imports


# Django imports
from django.urls import reverse


# Third party apps imports
from model_mommy import mommy
from model_mommy.random_gen import gen_email, gen_integer, gen_string
from rest_framework import status
from rest_framework.test import APITestCase


# Local imports
from apps.products.models import Model


# Create your viewset tests here.
class OrderTestCase(APITestCase):
    def setUp(self):
        self.model_1 = mommy.make(Model, _fill_optional=True, make_m2m=True)
        self.model_2 = mommy.make(Model, _fill_optional=True, make_m2m=True)
        self.model_3 = mommy.make(Model, _fill_optional=True, make_m2m=True)
        self.orders_url = reverse("api_v1:orders-list")

    def test_cant_get_response(self):
        response = self.client.get(self.orders_url)
        self.assertEqual(
            response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_create_order(self):
        data = {
            "client": {
                "cellphone": gen_string(50),
                "email": gen_email(),
                "first_name": gen_string(50),
                "last_name": gen_string(50),
            },
            "model": [self.model_1.id, self.model_2.id, self.model_3.id],
            "mount": gen_integer(0),
        }
        response = self.client.post(self.orders_url, data=data, format="json")
        self.assertEqual(
            response.status_code, status.HTTP_201_CREATED)
