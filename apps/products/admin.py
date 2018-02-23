# Python imports


# Django imports
from django.contrib import admin


# Third party apps imports


# Local imports
from .models import Color, Kind, Model, Product, Size


# Register your models here.
@admin.register(Model)
class ModelModelAdmin(admin.ModelAdmin):
    list_display = ("product", "image_admin_thumbnail",)


@admin.register(Kind)
class KindModelAdmin(admin.ModelAdmin):
    list_display = ("name", "category",)


@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ("name", "kind", "views",)
    exclude = ("views",)


admin.site.register(Color)
admin.site.register(Size)
