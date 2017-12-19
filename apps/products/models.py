# Python imports


# Django imports
from django.core.exceptions import ValidationError
from django.db import models


# Third party apps imports
from model_utils.models import TimeStampedModel


# Local imports


# Create your models here.
class Kind(TimeStampedModel):
    MALE = "hombre"
    FEMALE = "mujer"
    BOY = "niño"
    GIRL = "niña"

    CATEGORY_CHOICES = (
        (MALE, "Hombre"),
        (FEMALE, "Mujer"),
        (BOY, "Niño"),
        (GIRL, "Niña"),)

    category = models.CharField(
        max_length=6, choices=CATEGORY_CHOICES, verbose_name="categoría")
    name = models.CharField(max_length=50, unique=True, verbose_name="nombre")

    class Meta:
        verbose_name = "Tipo"
        ordering = ["-name", "category"]

    def __str__(self):
        return "{0}, {1}".format(self.name, self.category)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if Kind.objects.filter(name=self.name).exists():
            raise ValidationError(
                "No puede haber mas de un tipo con el mismo nombre")
        return super().save()

    @property
    def products(self):
        return self.product_set.all()


class Product(TimeStampedModel):
    available = models.PositiveSmallIntegerField(verbose_name="disponible")
    code = models.CharField(max_length=10, verbose_name="código", unique=True)
    description = models.TextField(verbose_name="descripción")
    donations = models.PositiveSmallIntegerField(
        verbose_name="donaciones", default=0)
    kind = models.ForeignKey("Kind", verbose_name="tipo")
    name = models.CharField(max_length=50, verbose_name="nombre")
    offer = models.PositiveSmallIntegerField(verbose_name="oferta", default=0)
    price = models.PositiveSmallIntegerField(verbose_name="precio", default=0)
    stock = models.PositiveSmallIntegerField(default=0)
    views = models.PositiveSmallIntegerField(verbose_name="vistas", default=0)

    class Meta:
        verbose_name = "Producto"
        ordering = ["-name", "kind"]
        unique_together = ("kind", "name",)

    def __str__(self):
        return self.name
    #
    # def save(self):
    #     return super(Product, self).save()
    #
    # @models.permalink
    # def get_absolute_url(self):
    #     return ("")
