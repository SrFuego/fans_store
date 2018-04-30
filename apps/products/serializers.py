# Python imports


# Django imports


# Third party apps imports
from rest_framework import serializers


# Local imports
from .models import Color, Kind, Model, Product, Size


# Create your serializers here.
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
    size = serializers.SerializerMethodField()

    class Meta:
        model = Model
        # fields = "__all__"
        fields = (
            "available", "color", "image", "offer", "price", "size", "stock",)

    def get_size(self, obj):
        return obj.size.all().values_list("name", flat=True)


class ProductSerializer(serializers.ModelSerializer):
    models = ModelSerializer(many=True)

    class Meta:
        model = Product
        # fields = "__all__"
        # depth = 3
        fields = ("id", "name", "description", "donations", "kind", "models",)


class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = ("id", "name",)
