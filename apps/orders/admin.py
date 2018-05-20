# Python imports


# Django imports
from django.contrib import admin


# Third party apps imports
from import_export.admin import ExportMixin
from import_export.formats import base_formats


# Local imports
from .models import Client, Order
from .resources import ClientResource, OrderResource


# Register your models here.
@admin.register(Client)
class ClientModelAdmin(ExportMixin, admin.ModelAdmin):
    formats = (base_formats.XLS,)
    list_display = ("full_name", "cellphone", "email")
    resource_class = ClientResource


@admin.register(Order)
class OrderModelAdmin(ExportMixin, admin.ModelAdmin):
    formats = (base_formats.XLS,)
    list_display = ("client", "mount", "delivered",)
    resource_class = OrderResource
