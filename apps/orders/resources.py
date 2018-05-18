# Python imports


# Django imports


# Third party apps imports
from import_export.fields import Field
from import_export.resources import ModelResource


# Local imports
from .models import Order


# Create your resources here.
class OrderResource(ModelResource):
    full_name = Field(attribute="client__full_name", column_name="Nombres")
    email = Field(attribute="client__email", column_name="Correo")
    cellphone = Field(attribute="client__cellphone", column_name="Celular")
    delivered = Field(attribute="delivered", column_name="Entregado")
    mount = Field(attribute="mount", column_name="Total")

    class Meta:
        model = Order
        fields = (
            "full_name", "email", "cellphone", "model", "delivered", "mount",)
