# Python imports


# Django imports


# Third party apps imports
from rest_framework.serializers import ModelSerializer
from rest_framework.utils import model_meta


# Local imports
from .models import Client, Order


# Create your serializers here.
class ClientSerializer(ModelSerializer):
    class Meta:
        model = Client
        fields = ("cellphone", "email", "first_name", "last_name",)


class OrderSerializer(ModelSerializer):
    client = ClientSerializer()

    class Meta:
        model = Order
        fields = ("client", "model", "mount",)

    def create(self, validated_data):
        client_data = validated_data.pop("client")
        client, created = Client.objects.get_or_create(**client_data)
        validated_data["client"] = client

        # Remove many-to-many relationships from validated_data.
        # They are not valid arguments to the default `.create()` method,
        # as they require that the instance has already been saved.
        info = model_meta.get_field_info(Order)
        many_to_many = {}
        for field_name, relation_info in info.relations.items():
            if relation_info.to_many and (field_name in validated_data):
                many_to_many[field_name] = validated_data.pop(field_name)

        instance = Order.objects.create(**validated_data)

        if many_to_many:
            for field_name, value in many_to_many.items():
                field = getattr(instance, field_name)
                field.set(value)

        return instance
