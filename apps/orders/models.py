# Python imports


# Django imports
from django.db import models


# Third party apps imports
from model_utils.models import TimeStampedModel


# Local imports


# Create your models here.
class Order(TimeStampedModel):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    size = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Pedido"

    def __str__(self):
        return self.name
