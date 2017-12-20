# Python imports


# Django imports
from django.contrib import admin


# Third party apps imports


# Local imports
from .models import Image, Kind, Product


# Register your models here.
@admin.register(Image)
class ImageModelAdmin(admin.ModelAdmin):
    list_display = ("product", "image_admin_thumbnail",)


@admin.register(Kind)
class KindModelAdmin(admin.ModelAdmin):
    list_display = ("name", "category",)


@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ("name", "kind", "price", "stock", "views",)
    exclude = ("views",)
