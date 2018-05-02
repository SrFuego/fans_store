# Python imports


# Django imports


# Third party apps imports
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, ViewSet


# Local imports
from .filtersets import ProductFilter
from .models import Collection, Color, Kind, Product, Size
from .serializers import (
    CollectionSerializer, ColorSerializer, KindSerializer, ProductSerializer,
    SizeSerializer,)


# Create your viewsets here.
class CollectionViewSet(ModelViewSet):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer
    http_method_names = ["get"]


class ColorViewSet(ModelViewSet):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer
    http_method_names = ["get"]


class KindViewSet(ModelViewSet):
    queryset = Kind.objects.all()
    serializer_class = KindSerializer
    http_method_names = ["get"]


class MostViewedViewSet(ViewSet):
    http_method_names = ["get"]

    def list(self, request, *args, **kwargs):
        queryset = Product.objects.most_viewed()
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)


class NewersViewSet(ViewSet):
    http_method_names = ["get"]

    def list(self, request, *args, **kwargs):
        queryset = Product.objects.newers()
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_class = ProductFilter
    http_method_names = ["get"]

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.views += 1
        instance.save(update_fields=["views"])
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class SizeViewSet(ModelViewSet):
    queryset = Size.objects.all()
    serializer_class = SizeSerializer
    http_method_names = ["get"]
