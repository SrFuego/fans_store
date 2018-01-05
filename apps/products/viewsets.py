# Python imports


# Django imports


# Third party apps imports
from rest_framework.viewsets import ModelViewSet


# Local imports
from .models import Kind
from .serializers import KindSerializer


# Create your viewsets here.
class KindViewSet(ModelViewSet):
    queryset = Kind.objects.all()
    serializer_class = KindSerializer
    http_method_names = [u'get']
