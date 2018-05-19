# Python imports


# Django imports
from django.core.exceptions import ValidationError
from django.test import TestCase
from django.utils import timezone


# Third party apps imports
from model_mommy import mommy
from model_mommy.random_gen import gen_string


# Local imports
from ..models import Client, Order
mommy.generators.add("model_utils.models.AutoCreatedField", timezone.now)
mommy.generators.add("model_utils.models.AutoLastModifiedField", timezone.now)


# Create your model tests here.
class ClientTestCase(TestCase):
    def setUp(self):
        self.client = mommy.make(Client, _fill_optional=True)

    def test_method_str_return_full_name(self):
        self.assertEqual(self.client.full_name, self.client.__str__())

    def test_cant_create_without_cellphone_or_email(self):
        data = {
            "first_name": gen_string(50),
            "last_name": gen_string(50)}
        self.assertRaises(ValidationError, Client.objects.create, **data)

    def tearDown(self):
        self.client.delete()


class OrderTestCase(TestCase):
    def setUp(self):
        self.client = mommy.make(Client, _fill_optional=True)
        self.order = mommy.make(Order, client=self.client, _fill_optional=True)

    def test_method_str_return_client_full_name(self):
        self.assertEqual(self.client.full_name, self.order.__str__())

    def tearDown(self):
        self.client.delete()
        self.order.delete()
