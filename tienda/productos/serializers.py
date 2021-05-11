from rest_framework import serializers
from .models import *
from usuarios.models import Usuario


class SerializerCreateProductoIn(serializers.Serializer):
    nombreProducto = serializers.CharField()
    descripcion = serializers.CharField()
    precio = serializers.FloatField()
    usuario_id = serializers.IntegerField()


    def save(self, **kwargs):
        Productos.objects.create_product(**self.validated_data)


    def update(self, instance, validated_data):
           instance.nombreProducto = validated_data.get('nombreProducto', instance.nombreProducto)
           instance.descripcion = validated_data.get('descripcion', instance.descripcion)
           instance.precio = validated_data.get('precio', instance.precio)
           instance.usuario = validated_data.get('usuario', instance.usuario)


class SerializerCreateProductoOut(serializers.Serializer):
    id = serializers.ReadOnlyField()
    nombreProducto = serializers.CharField()
    descripcion = serializers.CharField()
    precio = serializers.FloatField()
    usuario = serializers.SerializerMethodField()


    def get_usuario(self, obj: usuario ):
        try:
            instance = Usuario.Objects.get(id = obj.usuario_id)
            return instance.username
        except:
            return "No hay usuario"
