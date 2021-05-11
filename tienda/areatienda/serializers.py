from rest_framework import serializers
from areatienda.models import *
from .models import *


class SerializerCreateAreaIn(serializers.Serializer):
    nombreArea = serializers.CharField()
    users = serializers.ReadOnlyField()

    def save(self, **kwargs):
        Tienda.objects.create_area(
            nombreArea= self.validated_data.get("nombreArea"),
            user= self.validated_data.get("user"),
        )

    def update(self, instance, validated_data):
       instance.nombreArea = validated_data.get('nombreArea', instance.nombreArea)
       instance.user = validated_data.get('user', instance.user)



class SerializerCreateAreaOut(serializers.Serializer):
    id = serializers.ReadOnlyField()
    nombreArea = serializers.CharField()
    users = serializers.ReadOnlyField()
