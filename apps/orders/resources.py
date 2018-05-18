# Python imports


# Django imports


# Third party apps imports
from import_export import resources


# Local imports
from .models import Order


# Create your resources here.
class OrderResource(resources.ModelResource):
    class Meta:
        model = Order
        fields = ("id", "name", "phone", "size",)
