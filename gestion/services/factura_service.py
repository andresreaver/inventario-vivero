from gestion.models.factura import Factura, Detalle_factura
from gestion.models.producto import Producto
from django.db import transaction


class FacturaService:
    @staticmethod
    @transaction.atomic
    def crear_factura(cliente, forma_pago, detalles):
        print(f"Creando factura para cliente: {cliente.nombre_razon_social}, Forma de pago: {forma_pago}")
        # Crear la factura
        factura = Factura.objects.create(
            cliente=cliente,
            forma_pago=forma_pago,
            subtotal=0,
            iva=0,
            total=0
        )
        print(f"Factura creada con ID: {factura.numero_factura}")

        subtotal = 0
        for detalle in detalles:
            producto = detalle['producto']
            cantidad = detalle['cantidad']

            # Validar stock
            if producto.stock < cantidad:
                raise ValueError(f"No hay suficiente stock para {producto.nombre}")

            # Actualizar stock
            producto.stock -= cantidad
            producto.save()

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
        print(f"Subtotal calculado: {subtotal}")

        iva = subtotal * 0.19
        total = subtotal + iva

        # Actualizar totales de la factura
        factura.subtotal = subtotal
        factura.iva = iva
        factura.total = total
        factura.save()
        print(f"Factura actualizada con Total: {factura.total}")
        return factura

    @staticmethod
    def obtener_facturas():
        """
        Obtener todas las facturas con sus clientes relacionados.

        Returns:
            QuerySet: Lista de facturas con relación al cliente.
        """
        return Factura.objects.select_related('cliente').all()
