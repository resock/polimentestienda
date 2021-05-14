from django.db import models
#from usuarios.models import Usuario


# Create your models here.

class ProductoManager(models.Manager):
    def create_product(self, nombreProducto, descripcion, precio):
        if not precio:
            raise ValueError('Debe ingresar el precio del producto')
        producto = self.model(
            nombreProducto = nombreProducto,
            descripcion = descripcion,
            precio =precio,
        )
        producto.save()
        return producto



class Productos(models.Model):
    id = models.AutoField(primary_key= True)
    nombreProducto = models.CharField(max_length= 30)
    descripcion = models.CharField(max_length= 100)
    precio = models.FloatField(max_length= 10)


    objects = ProductoManager()
