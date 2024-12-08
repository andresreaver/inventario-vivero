from django.contrib import admin
from .models import Producto, Proveedor, Compra, Venta

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'tipo', 'stock', 'stock_minimo', 'fecha_caducidad', 'stock_bajo')
    search_fields = ('nombre', 'tipo')
    list_filter = ('nombre', )

@admin.register(Proveedor)
class ProveedorAdin(admin.ModelAdmin):
    list_display = ('nombre', 'telefono', 'email')
    search_fields = ('nombre', )

@admin.register(Compra)
class CompraAdmin(admin.ModelAdmin):
    list_display = ('proveedor', 'producto', 'cantidad', 'precio_unitario', 'fecha')
    list_filter = ('fecha', 'proveedor')

@admin.register(Venta)
class VentaAdmin(admin.ModelAdmin):
    list_display = ('producto', 'cantidad', 'precio_unitario', 'fecha')
    list_filter = ('fecha', )

#Register your Models Here
