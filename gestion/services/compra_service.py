from django.db import transaction
from gestion.models import Compra, Producto, Proveedor


class CompraService:
    """
    Servicio para gestionar operaciones relacionadas con las compras.
    """

    @staticmethod
    @transaction.atomic
    def registrar_compra(proveedor_id, producto_id, cantidad, precio_unitario):
        """
        Registra una nueva compra y actualiza el inventario del producto.

        :param proveedor_id: ID del proveedor.
        :param producto_id: ID del producto.
        :param cantidad: Cantidad comprada.
        :param precio_unitario: Precio unitario del producto.
        :raises ValueError: Si el producto no existe o los datos son inválidos.
        :return: La instancia de la compra registrada.
        """
        # Validar proveedor
        proveedor = Proveedor.objects.filter(id=proveedor_id).first()
        if not proveedor:
            raise ValueError("El proveedor especificado no existe.")

        # Validar producto
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
        """
        Obtiene la lista de todas las compras.

        :return: QuerySet con todas las compras.
        """
        return Compra.objects.select_related('proveedor', 'producto').all()