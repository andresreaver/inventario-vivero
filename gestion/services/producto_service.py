from gestion.models import Producto

class ProductoService:
    @staticmethod
    def crear_producto(nombre, tipo, stock, stock_minimo, fecha_caducidad=None):
        """Crea un nuevo producto."""
        producto = Producto.objects.create(
            nombre=nombre,
            tipo=tipo,
            stock=stock,
            stock_minimo=stock_minimo,
            fecha_caducidad=fecha_caducidad
        )
        return producto

    @staticmethod
    def ajustar_stock(producto_id, cantidad):
        """Ajusta el stock de un producto."""
        producto = Producto.objects.get(id=producto_id)
        producto.stock += cantidad
        producto.save()
        return producto

    @staticmethod
    def obtener_productos():
        """Devuelve una lista de todos los productos."""
        return Producto.objects.all()
