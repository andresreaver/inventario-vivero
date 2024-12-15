from gestion.models.compra import Compra
from gestion.models.proveedor import Proveedor
from gestion.models.producto import Producto

class CompraService:
    @staticmethod
    def listar_compras():
        """
        Devuelve todas las compras con proveedores y productos relacionados.
        """
        return Compra.objects.select_related('proveedor', 'producto').all()

    @staticmethod
    def crear_compra(data):
        """
        Crea una nueva compra.
        """
        proveedor = Proveedor.objects.get(id=data['proveedor_id'])
        producto = Producto.objects.get(id=data['producto_id'])

        return Compra.objects.create(
            proveedor=proveedor,
            producto=producto,
            cantidad=data['cantidad'],
            precio_unitario=data['precio_unitario'],
            numero_factura=data['numero_factura'],
            fecha=data['fecha']
        )
