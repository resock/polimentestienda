from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from .serializers import *
from .models import *
from rest_framework.response import Response
# Create your views here.

class CreateArea(viewsets.GenericViewSet):
    serializer_class = SerializerCreateAreaIn
    queryset = Tienda.objects.all()

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"status": "Area Registrado"}, status = status.HTTP_201_CREATED)


    def list(self, request):
        query = Tienda.objects.all()
        serializer = SerializerCreateAreaOut(query, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def put(self, request, *args, **kwargs, ):
        instance = get_object_or_404(Tienda, pk=request.data['id'])
        serializer = SerializerCreateAreaIn(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.update(instance, serializer.validated_data)
            return Response({"status": "Area Actualizada", "data": serializer.data}, status.HTTP_200_OK)


    def delete(self, request,  *args, **kwargs):
        instance = get_object_or_404(Tienda,  pk= request.data['id'])
        instance.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
