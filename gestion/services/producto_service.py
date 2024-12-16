from gestion.models.producto import Producto

class ProductoService:
    @staticmethod
    def crear_producto(nombre, tipo, stock, stock_minimo, fecha_caducidad=None):
        """Crea un nuevo producto."""
        return Producto.objects.create(
            nombre=nombre,
            tipo=tipo,
            stock=stock,
            stock_minimo=stock_minimo,
            fecha_caducidad=fecha_caducidad
        )

    @staticmethod
    def obtener_producto_por_id(producto_id):
        """Obtiene un producto por su ID."""
        return Producto.objects.get(id=producto_id)

    @staticmethod
    def obtener_productos():
        """Devuelve una lista de todos los productos."""
        return Producto.objects.all()

    @staticmethod
    def actualizar_producto(producto_id, **datos):
        """Actualiza un producto existente."""
        producto = Producto.objects.get(id=producto_id)
        for key, value in datos.items():
            setattr(producto, key, value)
        producto.save()
        return producto

    @staticmethod
    def eliminar_producto(producto_id):
        """Elimina un producto existente."""
        producto = Producto.objects.get(id=producto_id)
        producto.delete()
