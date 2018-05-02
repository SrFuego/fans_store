# Python imports


# Django imports
from django.contrib import admin
from django.db import models
from django.forms import CheckboxSelectMultiple


# Third party apps imports


# Local imports
from .models import Collection, Color, Kind, Model, Product, Size


# Register your models here.
@admin.register(Model)
class ModelModelAdmin(admin.ModelAdmin):
    list_display = ("product", "image_admin_thumbnail",)
    formfield_overrides = {
        models.ManyToManyField: {"widget": CheckboxSelectMultiple},
    }


@admin.register(Kind)
class KindModelAdmin(admin.ModelAdmin):
    list_display = ("name", "category",)


@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ("name", "kind", "views",)
    exclude = ("views",)


admin.site.register(Collection)
admin.site.register(Color)
admin.site.register(Size)
