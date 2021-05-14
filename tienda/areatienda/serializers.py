from rest_framework import serializers
from areatienda.models import *
from .models import *
from productos.models import Productos
from productos.serializers import SerializerCreateProductoOut


class SerializerCreateAreaIn(serializers.Serializer):
    nombreArea = serializers.CharField()
    producto_id = serializers.IntegerField()

    def save(self, **kwargs):
        Tienda.objects.create_area(**self.validated_data)

    def update(self, instance, validated_data):
       instance.nombreArea = validated_data.get('nombreArea', instance.nombreArea)


class SerializerCreateAreaOut(serializers.Serializer):
    id = serializers.ReadOnlyField()
    nombreArea = serializers.CharField()
    producto = serializers.SerializerMethodField()

    def get_producto(self, obj: producto):
        try:
            instance = Productos.objects.get(id = obj.producto_id)
            return SerializerCreateProductoOut(instance).data
        except:
            return "No hay producto"



