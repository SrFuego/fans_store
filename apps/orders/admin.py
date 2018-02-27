# Python imports


# Django imports
from django.contrib import admin


# Third party apps imports


# Local imports
from .models import Order


# Register your models here.
@admin.register(Order)
class OrderModelAdmin(admin.ModelAdmin):
    list_display = ("name", "size",)
