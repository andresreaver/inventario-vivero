from gestion.factura.factura import Factura

class FacturaService:
    @staticmethod
    def crear_factura(cliente, total):
        factura = Factura(cliente=cliente, total=total)
        factura.save()
        return factura

    @staticmethod
    def obtener_facturas():
        return Factura.objects.select_related('cliente').all()
