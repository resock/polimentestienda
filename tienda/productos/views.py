from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from .serializers import *
from .models import *
from rest_framework.response import Response
from usuarios.models import Usuario

# Create your views here.

class CreateProduct(viewsets.GenericViewSet):
    serializer_class = SerializerCreateProductoIn
    queryset = Productos.objects.all()


    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"status": "Producto Registrado"}, status = status.HTTP_201_CREATED)


    def list(self, request):
        query = Productos.objects.all()
        serializer = SerializerCreateProductoOut(query, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def put(self, request, *args, **kwargs, ):
        instance = get_object_or_404(Productos, pk=request.data['id'])
        serializer = SerializerCreateProductoIn(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.update(instance, serializer.validated_data)
            return Response({"status": "Producto Actualizado", "data": serializer.data}, status.HTTP_200_OK)


    def delete(self, request,  *args, **kwargs):
        instance = get_object_or_404(Productos,  pk= request.data['id'])
        instance.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)





