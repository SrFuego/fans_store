# Python imports


# Django imports
from django.core.exceptions import ValidationError
from django.test import TestCase


# Thirod party apps imports
from model_mommy import mommy


# Local imports
from ..models import Kind


# Create your model tests here.
class KindTestCase(TestCase):
    def setUp(self):
        self.kind = mommy.make(Kind)

    def test_method_str_return_name(self):
        self.assertEqual(self.kind.__str__(), self.kind.name)

    def test_there_should_not_be_two_types_with_the_same_name(self):
        kind_name = self.kind.name
        with self.assertRaises(ValidationError):
            Kind.objects.create(name=kind_name)

    def tearDown(self):
        self.kind.delete()
