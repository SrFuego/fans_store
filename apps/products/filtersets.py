# Python imports


# Django imports


# Third party apps imports
from django_filters import rest_framework as filters


# Local imports
from .models import Color, Kind, Product, Size


# Create your filter sets here.
class ProductFilter(filters.FilterSet):
    kind__name = filters.ChoiceFilter(
        label="kind__name",
        choices=tuple(
            [(kind, kind) for kind in
                set(Kind.objects.all().values_list("name", flat=True))]))
    kind__category = filters.ChoiceFilter(
        label="kind__category", choices=Kind.CATEGORY_CHOICES)
    model__color = filters.ModelChoiceFilter(
        label="model__color", queryset=Color.objects.all())
    model__size = filters.ModelChoiceFilter(
        label="model__size", queryset=Size.objects.all())

    class Meta:
        model = Product
        fields = ("kind__name", "kind__category", "model__color", "model__size")
