from rest_framework import serializers
from .models import *


class SerializerCreateProductoIn(serializers.Serializer):
    nombreProducto = serializers.CharField()
    descripcion = serializers.CharField()
    precio = serializers.FloatField()


    def save(self, **kwargs):
        Productos.objects.create_product(**self.validated_data)


    def update(self, instance, validated_data):
           instance.nombreProducto = validated_data.get('nombreProducto', instance.nombreProducto)
           instance.descripcion = validated_data.get('descripcion', instance.descripcion)
           instance.precio = validated_data.get('precio', instance.precio)


class SerializerCreateProductoOut(serializers.Serializer):
    id = serializers.ReadOnlyField()
    nombreProducto = serializers.CharField()
    descripcion = serializers.CharField()
    precio = serializers.FloatField()

