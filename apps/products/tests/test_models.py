# Python imports


# Django imports
from django.core.exceptions import ValidationError
from django.test import TestCase


# Thirod party apps imports
from model_mommy import mommy


# Local imports
from ..models import Color, Kind, Model, Product, Size


# Create your model tests here.
class ColorTestCase(TestCase):
    def setUp(self):
        self.color = mommy.make(Color)

    def test_method_str_return_name_and_category(self):
        self.assertTrue(self.color.name in self.color.__str__())

    def tearDown(self):
        self.color.delete()


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

    def test_have_queryset_models(self):
        self.assertTrue(self.product.models.model is Model)

    def tearDown(self):
        self.product.delete()


class SizeTestCase(TestCase):
    def setUp(self):
        self.size = mommy.make(Size)

    def test_method_str_return_name_and_category(self):
        self.assertTrue(self.size.name in self.size.__str__())

    def tearDown(self):
        self.size.delete()
