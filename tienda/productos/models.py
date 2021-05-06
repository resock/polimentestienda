from django.db import models
from usuarios.models import Usuario


# Create your models here.

class ProductoManager(models.Manager):
    def create_product(self, nombreProducto, descripcion, precio, usuario):
        if not precio:
            raise ValueError('Debe ingresar el precio del producto')
        producto = self.model(
            nombreProducto = nombreProducto,
            descripcion = descripcion,
            precio =precio,
            usuario= usuario,
        )
        producto.save()
        return producto



class Productos(models.Model):
    id = models.AutoField(primary_key= True)
    nombreProducto = models.CharField(max_length= 30)
    descripcion = models.CharField(max_length= 100)
    precio = models.FloatField(max_length= 10)
    usuario = models.ForeignKey(Usuario, related_name= 'usuarios', on_delete= models.SET_NULL,  null= True)


    objects = ProductoManager()
