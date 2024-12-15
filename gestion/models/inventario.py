from django.db import models
from django.contrib.auth import get_user_model
from gestion.models.producto import Producto


class MovimientoInventario(models.Model):
    TIPO_MOVIMIENTO = [('compra', 'Compra'), ('venta', 'Venta')]

    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    tipo_movimiento = models.CharField(max_length=10, choices=TIPO_MOVIMIENTO)
    cantidad = models.PositiveIntegerField()
    fecha = models.DateTimeField(auto_now_add=True)
    cliente = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True, blank=True)
    tipo_pago = models.CharField(max_length=50, blank=True, null=True)
    precio_total = models.DecimalField(max_digits=10, decimal_places=2)

    def __init__(self, *args: any, **kwargs: any):
        super().__init__(args, kwargs)
        self.precio_unitario = None

    def registrar_movimiento(self, tipo, cantidad, cliente=None, tipo_pago=None):
        if tipo == 'venta' and cantidad > self.stock_actual:
            raise ValueError("No hay suficiente stock.")
        self.stock_actual = self.stock_actual + cantidad if tipo == 'compra' else self.stock_actual - cantidad
        self.save()

        MovimientoInventario.objects.create(
            producto=self,
            tipo_movimiento=tipo,
            cantidad=cantidad,
            cliente=cliente,
            tipo_pago=tipo_pago,
            precio_total=cantidad * self.precio_unitario
        )