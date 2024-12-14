from django.db import models

class MateriaPrima(models.Model):
    nombre = models.CharField(max_length=200, unique=True)
    stock = models.PositiveIntegerField(default=0)
    stock_minimo = models.PositiveIntegerField(default=0)
    proveedor = models.ForeignKey('Proveedor', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.nombre

    def stock_bajo(self):
        return self.stock < self.stock_minimo
