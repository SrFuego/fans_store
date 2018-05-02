# Python imports


# Django imports
from django.test import TestCase


# Third party apps imports
from model_mommy import mommy


# Local imports
from ..models import Order


# Create your model tests here.
class OrderTestCase(TestCase):
    def setUp(self):
        self.order = mommy.make(Order)

    def test_method_str_return_name_and_category(self):
        self.assertTrue(self.order.name in self.order.__str__())

    def tearDown(self):
        self.order.delete()
