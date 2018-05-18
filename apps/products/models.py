# Python imports


# Django imports
from django.db import models
from django.utils.html import format_html


# Third party apps imports
from model_utils.models import TimeStampedModel
from stdimage.models import StdImageField
from stdimage.utils import UploadToAutoSlugClassNameDir


# Local imports
from .managers import ProductManager


# Create your models here.
class Collection(TimeStampedModel):
    name = models.CharField(unique=True, max_length=50, verbose_name="nombre")

    class Meta:
        verbose_name = "Colección"
        verbose_name_plural = "Colecciones"

    def __str__(self):
        return self.name


class Color(TimeStampedModel):
    name = models.CharField(unique=True, max_length=20, verbose_name="nombre")

    class Meta:
        verbose_name_plural = "Colores"

    def __str__(self):
        return self.name


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
    name = models.CharField(max_length=50, verbose_name="nombre")

    class Meta:
        verbose_name = "Tipo"
        ordering = ["-name", "category"]
        unique_together = ("category", "name",)

    def __str__(self):
        return "{0}, {1}".format(self.name, self.category)

    @property
    def products(self):
        return self.product_set.all()


class Model(TimeStampedModel):
    available = models.PositiveSmallIntegerField(
        verbose_name="cantidad disponible")
    color = models.ForeignKey("Color")
    image = StdImageField(
        upload_to=UploadToAutoSlugClassNameDir(populate_from="product"),
        variations={"thumbnail": (200, 100), "medium": (500, 500)},
        verbose_name="imagen")
    offer = models.PositiveSmallIntegerField(
        default=0,
        verbose_name="precio oferta (dejar en 0 si no esta en oferta)")
    price = models.PositiveSmallIntegerField(default=0, verbose_name="precio")
    product = models.ForeignKey("Product", verbose_name="producto")
    size = models.ManyToManyField(
        "Size", related_name="sizes", verbose_name="talla")
    stock = models.PositiveSmallIntegerField(default=0)

    class Meta:
        verbose_name = "Modelo"

    def __str__(self):
        return "{0}, {1}".format(self.product.name, self.color)

    def image_admin_thumbnail(self):
        return format_html(  # pragma: no cover
            "<img src='{0}' alt='{1}'>", self.image.thumbnail.url,
            self.product.name)

    @property
    def sizes(self):
        return self.size.all().values_list("name", flat=True)


class Product(TimeStampedModel):
    code = models.CharField(max_length=10, unique=True, verbose_name="código")
    collection = models.ForeignKey("Collection", verbose_name="colección")
    description = models.TextField(verbose_name="descripción")
    donations = models.PositiveSmallIntegerField(
        default=0, verbose_name="donaciones")
    kind = models.ForeignKey("Kind", verbose_name="tipo")
    name = models.CharField(max_length=50, verbose_name="nombre")
    objects = ProductManager.as_manager()
    views = models.PositiveSmallIntegerField(default=0, verbose_name="vistas")

    class Meta:
        verbose_name = "Producto"
        ordering = ["-name", "kind"]
        unique_together = ("kind", "name",)

    def __str__(self):
        return self.name

    @property
    def models(self):
        return self.model_set.all()


class Size(TimeStampedModel):
    name = models.CharField(unique=True, max_length=10, verbose_name="nombre")

    class Meta:
        verbose_name = "Talla"

    def __str__(self):
        return self.name
