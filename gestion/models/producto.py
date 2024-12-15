from django.db import models
from gestion.managers import ProductoManager


class Producto(models.Model):
    nombre = models.CharField(max_length=200, unique=True)
    tipo = models.CharField(max_length=100)
    stock = models.IntegerField(default=0)
    stock_minimo = models.IntegerField(default=0)
    fecha_caducidad = models.DateField(null=True, blank=True)
    precio_compra = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    precio_venta = models.DecimalField(max_digits=10, decimal_places=2)
    activo = models.BooleanField(default=True)
    creado = models.DateTimeField(auto_now_add=True)
    modificado = models.DateTimeField(auto_now=True)

    # Manager personalizado
    objects = ProductoManager()

    def __str__(self):
        return self.nombre

    def stock_bajo(self):
        """
        Devuelve True si el stock actual está por debajo del stock mínimo.
        """
        return self.stock < self.stock_minimo

    def es_perecedero(self):
        """
        Verifica si el producto tiene una fecha de caducidad.
        """
        return self.fecha_caducidad is not None

    def tiempo_para_caducar(self):
        """
        Calcula el número de días restantes para la fecha de caducidad.
        Devuelve None si no tiene fecha de caducidad.
        """
        if self.fecha_caducidad:
            return (self.fecha_caducidad - timezone.now().date()).days
        return None
