from django.db import models

class ProductoManager(models.Manager):
    def con_stock_bajo(self):
        return self.filter(stock__lt=models.F('stock_minimo'))
