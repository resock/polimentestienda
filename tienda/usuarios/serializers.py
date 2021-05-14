from rest_framework import serializers
from .models import *
from areatienda.models import Tienda
from areatienda.serializers import SerializerCreateAreaOut

class SerializerCreateUserIn(serializers.Serializer):
    nombres= serializers.CharField()
    apellidos = serializers.CharField()
    username = serializers.CharField()
    password = serializers.CharField()
    email = serializers.EmailField()
    usuario_staff = serializers.BooleanField()
    usuario_admin = serializers.BooleanField()
    AreaTienda_id = serializers.IntegerField()

    def create(self):
        Usuario.Objects.create_user(**self.validated_data)
            #email= self.validated_data.get("email"),
            #nombres= self.validated_data.get("nombres"),
            #apellidos= self.validated_data.get("apellidos"),
            #username =  self.validated_data.get("username"),
            #usuario_staff = self.validated_data.get("usuario_staff"),
            #usuario_admin = self.validated_data.get("usuario_admin"),
            #password =  self.validated_data.get("password"),
            #AreaTienda_id=self.validated_data.get("AreaTienda"),


        #)

    def update(self, instance, validated_data):
        instance.nombres = validated_data.get('nombres', instance.nombres)
        instance.apellidos = validated_data.get('apellidos', instance.apellidos)
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.usuario_staff = validated_data.get('usuario_staff', instance.usuario_staff)
        instance.usuario_admin = validated_data.get('usuario', instance.usuario_admin)
        instance.AreaTienda = validated_data.get('AreaTienda', instance.AreaTienda)
        instance.save()

class SerializerCreateUserOut(serializers.Serializer):
    id = serializers.ReadOnlyField()
    nombres= serializers.CharField()
    apellidos = serializers.CharField()
    username = serializers.CharField()
    email = serializers.EmailField()
    usuario_staff = serializers.BooleanField()
    usuario_admin = serializers.BooleanField()
    AreaTienda = serializers.SerializerMethodField()

    def get_AreaTienda(self, obj: AreaTienda):
        try:
            instance = Tienda.objects.get(id = obj.AreaTienda_id)
            return SerializerCreateAreaOut(instance).data
        except:
            return "No tiene area asignada"
