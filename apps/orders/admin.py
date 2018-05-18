# Python imports


# Django imports
from django.contrib import admin


# Third party apps imports
from import_export.admin import ExportMixin


# Local imports
from .models import Order
from .resources import OrderResource


# Register your models here.
@admin.register(Order)
class OrderModelAdmin(ExportMixin, admin.ModelAdmin):
    resource_class = OrderResource
    list_display = ("name", "size",)
