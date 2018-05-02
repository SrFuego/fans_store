# Python imports


# Django imports


# Third party apps imports
from rest_framework import serializers


# Local imports
from .models import Collection, Color, Kind, Model, Product, Size


# Create your serializers here.
class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ("id", "name",)


class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = ("id", "name",)


class KindSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kind
        fields = ("id", "name", "category",)


class ModelSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(source="image.medium")
    color = serializers.CharField(source="color.name")

    class Meta:
        model = Model
        fields = (
            "available", "color", "image", "offer", "price", "sizes", "stock",)


class ProductSerializer(serializers.ModelSerializer):
    models = ModelSerializer(many=True)
    collection = serializers.CharField(source="collection.name")

    class Meta:
        model = Product
        fields = (
            "id", "name", "description", "donations", "collection", "kind",
            "models",)


class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = ("id", "name",)
