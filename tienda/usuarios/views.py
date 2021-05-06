from django.forms import modelform_factory
from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from rest_framework import viewsets, status
from .serializers import *
from rest_framework.response import Response



# Create your views here.

class createUser(viewsets.GenericViewSet):
    serializer_class = SerializerCreateUserIn
    queryset = Usuario.Objects.all()

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.create()
            return Response({"status": "Usuario Creado"}, status=status.HTTP_201_CREATED)


    def list(self, request):
        query = Usuario.Objects.all()
        serializer = SerializerCreateUserOut(query, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def put(self, request,*args, **kwargs, ):
        instance  = get_object_or_404(Usuario, pk = request.data['id'])
        serializer = SerializerCreateUserIn(data = request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.update(instance, serializer.validated_data)
            return Response({"status": "Usuario Actualizado", "data": serializer.data}, status.HTTP_200_OK)


    def delete(self, request,  *args, **kwargs):
        instance = get_object_or_404(Usuario,  pk= request.data['id'])
        instance.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)



