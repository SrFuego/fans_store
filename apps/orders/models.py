# Python imports


# Django imports
from django.core.exceptions import ValidationError
from django.db import models


# Third party apps imports
from model_utils.models import TimeStampedModel


# Local imports


# Create your models here.
class Client(TimeStampedModel):
    cellphone = models.CharField(
        max_length=50, blank=True, null=True, verbose_name="celular")
    email = models.EmailField(blank=True, null=True, verbose_name="correo")
    first_name = models.CharField(max_length=50, verbose_name="nombres")
    last_name = models.CharField(max_length=50, verbose_name="apellidos")

    class Meta:
        verbose_name = "Cliente"

    def __str__(self):
        return self.full_name

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if not any([self.cellphone, self.email]):
            raise ValidationError("El cliente debe tener celular o correo")
        return super().save()

    @property
    def full_name(self):
        return "{0}, {1}".format(self.last_name, self.first_name)


class Order(TimeStampedModel):
    client = models.ForeignKey("Client", verbose_name="cliente")
    delivered = models.BooleanField(default=False, verbose_name="entregado")
    model = models.ManyToManyField("products.Model", verbose_name="modelos")
    mount = models.PositiveSmallIntegerField(verbose_name="total")

    class Meta:
        verbose_name = "Pedido"

    def __str__(self):
        return self.client.full_name
