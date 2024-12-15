from gestion.models.factura import Factura, Detalle_factura
from gestion.models.producto import Producto
from django.db import transaction


class FacturaService:
    @staticmethod
    @transaction.atomic
    def crear_factura(cliente, forma_pago, detalles):
        """
        Crear una nueva factura para un cliente con los detalles dados.

        Args:
            cliente (Cliente): Instancia del cliente.
            forma_pago (str): Forma de pago de la factura.
            detalles (list): Lista de diccionarios con los productos y cantidades.
                Ejemplo: [{'producto': producto_obj, 'cantidad': 2}, ...]

        Returns:
            Factura: La factura creada.
        """
        # Crear la factura inicial sin totales
        factura = Factura(cliente=cliente, forma_pago=forma_pago)
        factura.save()

        subtotal = 0

        for detalle in detalles:
            producto = detalle['producto']
            cantidad = detalle['cantidad']

            # Validar stock del producto
            if producto.stock < cantidad:
                raise ValueError(f"El producto {producto.nombre} no tiene suficiente stock.")

            # Reducir stock del producto
            producto.stock -= cantidad
            producto.save()

            # Calcular subtotal para el detalle
            subtotal_detalle = producto.precio_venta * cantidad
            subtotal += subtotal_detalle

            # Crear el detalle de la factura
            Detalle_factura.objects.create(
                factura=factura,
                producto=producto,
                cantidad=cantidad,
                precio_unitario=producto.precio_venta,
                subtotal=subtotal_detalle
            )

        # Calcular impuestos y totales
        iva = subtotal * 0.19
        total = subtotal + iva

        # Actualizar los totales en la factura
        factura.subtotal = subtotal
        factura.iva = iva
        factura.total = total
        factura.save()

        return factura

    @staticmethod
    def obtener_facturas():
        """
        Obtener todas las facturas con sus clientes relacionados.

        Returns:
            QuerySet: Lista de facturas con relación al cliente.
        """
        return Factura.objects.select_related('cliente').all()
