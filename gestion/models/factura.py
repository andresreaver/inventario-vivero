from django.db import models

class Factura(models.Model):
    cliente = models.ForeignKey('Cliente', on_delete=models.CASCADE, related_name='facturas')
    fecha = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Factura #{self.id} - {self.cliente.nombre}"
