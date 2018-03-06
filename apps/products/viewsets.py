# Python imports


# Django imports


# Third party apps imports
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet


# Local imports
from .models import Kind, Product
from .serializers import KindSerializer, ProductSerializer


# Create your viewsets here.
class KindViewSet(ModelViewSet):
    queryset = Kind.objects.all()
    serializer_class = KindSerializer
    http_method_names = [u'get']


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_fields = ("kind",)
    http_method_names = [u'get']

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.views += 1
        instance.save(update_fields=["views"])
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
