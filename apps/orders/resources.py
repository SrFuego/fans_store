# Python imports


# Django imports


# Third party apps imports
from import_export.fields import Field
from import_export.resources import ModelResource


# Local imports
from .models import Client, Order


# Create your resources here.
class ClientResource(ModelResource):
    cellphone = Field(attribute="cellphone", column_name="Celular")
    email = Field(attribute="email", column_name="Correo")
    full_name = Field(attribute="full_name", column_name="Nombres")

    class Meta:
        model = Client
        fields = ("cellphone", "email", "full_name",)
        export_order = ("full_name", "cellphone", "email",)


class OrderResource(ModelResource):
    cellphone = Field(attribute="client__cellphone", column_name="Celular")
    delivered = Field(column_name="Entregado")
    email = Field(attribute="client__email", column_name="Correo")
    full_name = Field(attribute="client__full_name", column_name="Nombres")
    model = Field(column_name="Modelos")
    mount = Field(attribute="mount", column_name="Monto")

    class Meta:
        model = Order
        fields = (
            "cellphone", "delivered", "email", "full_name", "model", "mount",)
        export_order = (
            "full_name", "cellphone", "email", "model", "delivered", "mount",)

    def dehydrate_delivered(self, order):
        return "Si" if order.delivered else "No"

    def dehydrate_model(self, order):
        return "\n".join([model.__str__() for model in order.model.all()])
