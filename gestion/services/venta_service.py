from gestion.models import Venta


class VentaService:
    @staticmethod
    def registrar_venta(cliente, producto, cantidad):
        """Registra una nueva venta."""
        if producto.stock < cantidad:
            raise ValueError(f"Stock insuficiente para el producto {producto.nombre}")

        # Actualizar stock
        producto.stock -= cantidad
        producto.save()

        # Calcular precio total
        precio_total = producto.precio_unitario * cantidad  # Corregido aquí
        return Venta.objects.create(
            cliente=cliente,
            producto=producto,
            cantidad=cantidad,
            precio_unitario=producto.precio_unitario,  # Asegúrate de guardar también el precio unitario
            precio_total=precio_total
        )
