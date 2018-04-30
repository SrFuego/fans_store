# Python imports


# Django imports
from django.core.exceptions import ValidationError
from django.test import TestCase


# Thirod party apps imports
from model_mommy import mommy


# Local imports
from ..models import Kind, Product


# Create your model tests here.
class KindTestCase(TestCase):
    def setUp(self):
        self.kind = mommy.make(Kind)

    def test_method_str_return_name_and_category(self):
        self.assertTrue(self.kind.name in self.kind.__str__())
        self.assertTrue(self.kind.category in self.kind.__str__())

    def test_have_queryset_products(self):
        self.assertTrue(self.kind.products.model is Product)

    def tearDown(self):
        self.kind.delete()


class ProductTestCase(TestCase):
    def setUp(self):
        self.product = mommy.make(Product)

    def test_method_str_return_name(self):
        self.assertEqual(self.product.__str__(), self.product.name)

    def tearDown(self):
        self.product.delete()
