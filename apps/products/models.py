# Python imports


# Django imports
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.html import format_html


# Third party apps imports
from model_utils.models import TimeStampedModel
from stdimage.models import StdImageField
from stdimage.utils import UploadToAutoSlugClassNameDir
from stdimage.validators import MaxSizeValidator, MinSizeValidator


# Local imports


# Create your models here.
class Image(TimeStampedModel):
    image = StdImageField(
        upload_to=UploadToAutoSlugClassNameDir(populate_from="product"),
        validators=[MinSizeValidator(400, 250), MaxSizeValidator(1000, 1000)],
        variations={"thumbnail": (300, 200)}, verbose_name="imagen")
    product = models.ForeignKey("Product", verbose_name="producto")

    class Meta:
        verbose_name = "Imagen"
        verbose_name_plural = "Imágenes"

    # def __str__(self):
    #     return super().__str__()
    #
    # def save(self):
    #     return super().save()
    #
    # @models.permalink
    # def get_absolute_url(self):
    #     return ('')

    def image_admin_thumbnail(self):
        if self.image:
            return format_html(
                "<img src='{0}' alt='{1}'>", self.image.thumbnail.url,
                self.product.name)
        else:
            return "Sin imagen"


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
    code = models.CharField(max_length=10, unique=True, verbose_name="código")
    description = models.TextField(verbose_name="descripción")
    donations = models.PositiveSmallIntegerField(
        default=0, verbose_name="donaciones")
    kind = models.ForeignKey("Kind", verbose_name="tipo")
    name = models.CharField(max_length=50, verbose_name="nombre")
    offer = models.PositiveSmallIntegerField(default=0, verbose_name="oferta")
    price = models.PositiveSmallIntegerField(default=0, verbose_name="precio")
    stock = models.PositiveSmallIntegerField(default=0)
    views = models.PositiveSmallIntegerField(default=0, verbose_name="vistas")

    class Meta:
        verbose_name = "Producto"
        ordering = ["-name", "kind"]
        unique_together = ("kind", "name",)

    def __str__(self):
        return self.name

    # def save(self):
    #     return super(Product, self).save()

    @property
    def images(self):
        return self.image_set.all()
