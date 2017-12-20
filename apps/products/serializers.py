# Python imports


# Django imports


# Third party apps imports
from rest_framework.serializers import ModelSerializer


# Local imports
from .models import Image, Kind, Product


# Create your serializers here.
class ImageSerializer(ModelSerializer):
    class Meta:
        model = Image
        fields = ("image",)


class KindSerializer(ModelSerializer):
    class Meta:
        model = Kind
        fields = ("name", "category",)


class ProductSerializer(ModelSerializer):
    images = ImageSerializer(many=True)

    class Meta:
        model = Product
        fields = (
            "name", "description", "stock", "available", "donations", "price",
            "offer", "images",)
