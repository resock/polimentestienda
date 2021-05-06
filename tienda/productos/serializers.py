from rest_framework import serializers
from productos.models import *
from .models import *


class SerializerCreateProductoIn(serializers.Serializer):
   class Meta:
       model = Productos
       fields = '__all__'

   def create(self):
        Productos.objects.CreateProduct(
            nombreProducto = self.validated_data.get("nombreProducto"),
            descripcion = self.validated_data.get("descripcion"),
            precio = self.validated_data.get("precio"),
            usuario = self.validated_data.get("usuario"),
        )


   def update(self, instance, validated_data):
       instance.nombreProducto = validated_data.get('nombreProducto', instance.nombreProducto)
       instance.descripcion = validated_data.get('descripcion', instance.descripcion)
       instance.precio = validated_data.get('precio', instance.precio)
       instance.usuario = validated_data.get('usuario', instance.usuario)


class SerializerCreateProductoOut(serializers.Serializer):
    class Meta:
        model = Productos
        fields = '__all__'