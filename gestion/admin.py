from django.contrib import admin
from .models import Producto, Proveedor, Compra, Venta
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'tipo', 'stock', 'stock_minimo', 'fecha_caducidad', 'stock_bajo')
    search_fields = ('nombre', 'tipo')
    list_filter = ('nombre', )

@admin.register(Proveedor)
class ProveedorAdin(admin.ModelAdmin):
    list_display = ('nit_cedula', 'nombre_razon_social', 'telefono', 'correo_electronico', 'direccion')
    search_fields = ('nombre',)

@admin.register(Compra)
class CompraAdmin(admin.ModelAdmin):
    list_display = ('proveedor', 'producto', 'cantidad', 'precio_unitario', 'fecha')
    list_filter = ('fecha', 'proveedor')

@admin.register(Venta)
class VentaAdmin(admin.ModelAdmin):
    list_display = ('producto', 'cantidad', 'precio_unitario', 'fecha')
    list_filter = ('fecha', )

#Register your Models Here


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Información Adicional', {'fields': ('role',)}),
    )
