from django.db import models

# Create your models here.
class Producto(models.Model):
    codigo = models.CharField(primary_key= True,max_length =6)
    nombre = models.CharField(max_length =50)
    precio = models.PositiveIntegerField()
    cantidad = models.PositiveIntegerField()
    image = models.CharField(max_length =250)


    def __str__(self):
        return self.nombre