# Python imports


# Django imports


# Third party apps imports
from rest_framework.serializers import ModelSerializer


# Local imports
from .models import Client, Order
from ..products.serializers import ModelSerializer as ProductsModelSerializer


# Create your serializers here.
class ClientSerializer(ModelSerializer):
    class Meta:
        model = Client
        fields = "__all__"


class OrderSerializer(ModelSerializer):
    client = ClientSerializer()
    model = ProductsModelSerializer(many=True)

    class Meta:
        model = Order
        fields = "__all__"
