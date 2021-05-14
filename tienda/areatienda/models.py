from django.db import models
from productos.models import Productos

# Create your models here.

class TiendaManager(models.Manager):
    def create_area(self, nombreArea, producto_id):
        if not nombreArea:
            raise ValueError('Debe ingresar el nombre del area')
        area = self.model(
            nombreArea = nombreArea,
            producto_id = producto_id,
        )
        area.save()
        return area

class Tienda(models.Model):
    id = models.AutoField(primary_key = True)
    nombreArea =models.CharField(max_length=25)
    producto = models.ForeignKey(Productos, on_delete = models.SET_NULL, null = True)

    objects = TiendaManager()