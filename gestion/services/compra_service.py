from django.db import transaction
from gestion.models import Compra, Producto, Proveedor


class CompraService:
    @staticmethod
    @transaction.atomic
    def registrar_compra(proveedor_id, producto_id, cantidad, precio_unitario):
        proveedor = Proveedor.objects.filter(id=proveedor_id).first()
        if not proveedor:
            raise ValueError("El proveedor especificado no existe.")

        producto = Producto.objects.filter(id=producto_id).first()
        if not producto:
            raise ValueError("El producto especificado no existe.")

        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor a cero.")

        if precio_unitario <= 0:
            raise ValueError("El precio unitario debe ser mayor a cero.")

        # Crear la compra
        compra = Compra.objects.create(
            proveedor=proveedor,
            producto=producto,
            cantidad=cantidad,
            precio_unitario=precio_unitario,
        )

        # Actualizar el stock del producto
        producto.stock += cantidad
        producto.save()

        return compra

    @staticmethod
    def obtener_compras():
        return Compra.objects.select_related('proveedor', 'producto').all()
