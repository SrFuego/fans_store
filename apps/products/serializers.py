# Python imports


# Django imports


# Third party apps imports
from rest_framework.serializers import ModelSerializer


# Local imports
from .models import Kind


# Create your serializers here.
class KindSerializer(ModelSerializer):
    class Meta:
        model = Kind
        fields = "__all__"
