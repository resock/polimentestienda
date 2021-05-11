from rest_framework import serializers
from .models import *


class SerializerCreateUserIn(serializers.Serializer):
    #usuarios = serializers.StringRelatedField(many=True)
    nombres= serializers.CharField()
    apellidos = serializers.CharField()
    username = serializers.CharField()
    password = serializers.CharField()
    email = serializers.EmailField()
    usuario_staff = serializers.BooleanField()
    usuario_admin = serializers.BooleanField()

    def create(self):
        Usuario.Objects.create_user(
            email= self.validated_data.get("email"),
            nombres= self.validated_data.get("nombres"),
            apellidos= self.validated_data.get("apellidos"),
            username =  self.validated_data.get("username"),
            password =  self.validated_data.get("password"),

        )

    def update(self, instance, validated_data):
        instance.nombres = validated_data.get('nombres', instance.nombres)
        instance.apellidos = validated_data.get('apellidos', instance.apellidos)
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.usuario_staff = validated_data.get('usuario_staff', instance.usuario_staff)
        instance.usuario_admin = validated_data.get('usuario', instance.usuario_admin)
        instance.save()

class SerializerCreateUserOut(serializers.Serializer):
    id = serializers.ReadOnlyField()
    nombres= serializers.CharField()
    apellidos = serializers.CharField()
    username = serializers.CharField()
    email = serializers.EmailField()
    usuario_staff = serializers.BooleanField()
    usuario_admin = serializers.BooleanField()