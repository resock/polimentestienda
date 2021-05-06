from django.db import models
from usuarios.models import Usuario

# Create your models here.

class TiendaManager(models.Manager):
    def create_area(self, nombreArea, user):
        if not nombreArea:
            raise ValueError('Debe ingresar el nombre del area')
        area = self.model(
            nombreArea = nombreArea,
            user= user,
        )
        area.save()
        return area

class Tienda(models.Model):
    id = models.AutoField(primary_key = True)
    nombreArea =models.CharField(max_length=25)
    user = models.ForeignKey(Usuario, on_delete=models.SET_NULL,  null= True)

    objects = TiendaManager()