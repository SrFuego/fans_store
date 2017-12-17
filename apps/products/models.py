# Python imports


# Django imports
from django.db import models
from django.core.exceptions import ValidationError


# Third party apps imports
from model_utils.models import TimeStampedModel


# Local imports


# Create your models here.
class Kind(TimeStampedModel):
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        verbose_name = "Tipo"

    def __str__(self):
        return self.name

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
    name = models.CharField(max_length=50)
    kind = models.ForeignKey("Kind")

    class Meta:
        verbose_name = "Producto"

    def __str__(self):
        return self.name
    #
    # def save(self):
    #     return super(Product, self).save()
    #
    # @models.permalink
    # def get_absolute_url(self):
    #     return ("")
