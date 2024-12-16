from django.db import models
from django.utils.timezone import now
from gestion.models.cliente import Cliente
from gestion.models.producto import Producto

class Factura(models.Model):
    numero_factura = models.AutoField (primary_key=True)
    cliente = models.ForeignKey('Cliente', on_delete=models.CASCADE, related_name='facturas')
    fecha = models.DateTimeField(default=now)
    forma_pago = models.CharField(
        max_length=100,
        choices=[
            ('Efectivo', 'Efectivo'),
            ('Tarjeta de Credito', 'Tarjeta de Credito'),
            ('Tarjeta Debito', 'Tarjeta Debito')
        ]
    )
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    iva = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Factura #{self.id} - {self.cliente.nombre}"

class Detalle_factura(models.Model):
    factura = models.ForeignKey(Factura, related_name="detalles", on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)