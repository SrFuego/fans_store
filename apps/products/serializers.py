# Python imports


# Django imports


# Third party apps imports
from rest_framework import serializers


# Local imports
from .models import Kind, Model, Product


# Create your serializers here.
class ModelSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(source="image.medium")

    class Meta:
        model = Model
        fields = ("image",)


class KindSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kind
        fields = ("name", "category",)


class ProductSerializer(serializers.ModelSerializer):
    models = ModelSerializer(many=True)

    class Meta:
        model = Product
        fields = "__all__"
        # fields = (
        #     "name", "description", "stock", "available", "donations",
        #     "price",
        #     "offer", "images",)
