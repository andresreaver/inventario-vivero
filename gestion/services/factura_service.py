from gestion.models.factura import Factura, Detalle_factura
from gestion.models.producto import Producto
from django.db import transaction

class FacturaService:
    @staticmethod
    def crear_factura(cliente, forma_pago, detalles):

        with transaction.atomic():
            factura = Factura(cliente=cliente, forma_pago=forma_pago)
            factura.save()

            subtotal=0
            for detalle in detalles:
                producto =detalle['producto']
                cantidad =detalle['cantidad']

            if producto.stock < cantidad:
                raise ValueError(f"El producto {producto} no tiene suficiente stock.")

            producto.stock -= cantidad
            producto.save()

            subtotal_detalle = producto.precio_venta * cantidad
            DetalleFactura.object.create(
                factura=factura,
                producto=producto,
                cantidad=cantidad,
                precio_unitario=producto.precio_venta,
                subtotal=subtotal_detalle
            )
            subtotal += subtotal_detalle
            
        iva = subtotal * 0.19
        total = subtotal + iva

        factura.subtotal = subtotal
        factura.iva = iva
        factura.total = total
        factura.save()

        return factura

    @staticmethod
    def obtener_facturas():
        return Factura.objects.select_related('cliente').all()
