# Python imports


# Django imports
from rest_framework.generics import ListAPIView


# Third party apps imports


# Local imports
from .models import Product
from .serializers import ProductSerializer


# Create your views here.
class MostViewedAPIView(ListAPIView):
    queryset = Product.objects.all().order_by("views")[:6]
    serializer_class = ProductSerializer


class NewersAPIView(ListAPIView):
    queryset = Product.objects.all().order_by("created")[:6]
    serializer_class = ProductSerializer
