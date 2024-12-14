from gestion.models import Compra

class CompraService:
    @staticmethod
    def registrar_compra(proveedor, producto, cantidad, precio_unitario):
        """Registra una nueva compra."""
        compra = Compra.objects.create(
            proveedor=proveedor,
            producto=producto,
            cantidad=cantidad,
            precio_unitario=precio_unitario
        )
        return compra

    @staticmethod
    def obtener_compras():
        """Devuelve una lista de todas las compras."""
        return Compra.objects.all()
