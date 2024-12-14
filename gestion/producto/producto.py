from django.db import models
from gestion.managers import ProductoManager

class Producto(models.Model):
    nombre = models.CharField(max_length=200, unique=True)
    tipo = models.CharField(max_length=100)
    stock = models.IntegerField(default=0)
    stock_minimo = models.IntegerField(default=0)
    fecha_caducidad = models.DateField(null=True, blank=True)

    objects = ProductoManager()  # Manager personalizado

    def __str__(self):
        return self.nombre

    def stock_bajo(self):
        return self.stock < self.stock_minimo
