# Python imports


# Django imports


# Third party apps imports
from django_filters import rest_framework as filters


# Local imports
from .models import Color, Kind, Product, Size


# Create your filter sets here.
class ProductFilter(filters.FilterSet):
    kind = filters.ModelChoiceFilter(label="kind", queryset=Kind.objects.all())
    kind__category = filters.ChoiceFilter(
        label="kind__category", choices=Kind.CATEGORY_CHOICES)
    model__color = filters.ModelChoiceFilter(
        label="model__color", queryset=Color.objects.all())
    model__size = filters.ModelChoiceFilter(
        label="model__size", queryset=Size.objects.all())

    class Meta:
        model = Product
        fields = ("kind", "kind__category", "model__color", "model__size")
