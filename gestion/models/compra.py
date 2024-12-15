from django.db import models
from .proveedor import Proveedor  # Importa desde proveedor.py
from .producto import Producto


class Compra(models.Model):
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE, related_name='compras')
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name='compras')
    cantidad = models.PositiveIntegerField()
    fecha = models.DateTimeField(auto_now_add=True)
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.proveedor.nombre_razon_social} - {self.producto.nombre} ({self.cantidad})"

    def total(self):
        return self.cantidad * self.precio_unitario