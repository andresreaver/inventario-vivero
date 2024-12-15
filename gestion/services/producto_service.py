from django.shortcuts import get_object_or_404
from gestion.models.producto import Producto
from django.core.exceptions import ValidationError
from django.utils.timezone import now

class ProductoService:
    @staticmethod
    def crear_producto(nombre, tipo, stock=0, stock_minimo=0,
                       fecha_caducidad=None, precio_compra=None, precio_venta=None, activo=True):
        """
        Crea un nuevo producto después de validar los datos.
        Lanza una excepción ValidationError si los datos son inválidos.
        """
        if precio_venta is not None and precio_venta < 0:
            raise ValidationError("El precio de venta no puede ser negativo.")
        if stock < stock_minimo:
            raise ValidationError("El stock inicial no puede ser menor al stock mínimo.")
        if fecha_caducidad and fecha_caducidad < now().date():
            raise ValidationError("La fecha de caducidad no puede ser una fecha pasada.")

        return Producto.objects.create(
            nombre=nombre,
            tipo=tipo,
            stock=stock,
            stock_minimo=stock_minimo,
            fecha_caducidad=fecha_caducidad,
            precio_compra=precio_compra,
            precio_venta=precio_venta,
            activo=activo
        )

    @staticmethod
    def obtener_producto_por_id(producto_id):
        """
        Obtiene un producto por su ID o lanza un error 404 si no existe.
        """
        return get_object_or_404(Producto, id=producto_id)

    @staticmethod
    def obtener_productos(activos=True):
        """
        Devuelve una lista de productos.
        Si `activos` es True, devuelve solo los productos activos.
        """
        return Producto.objects.filter(activo=activos)

    @staticmethod
    def actualizar_producto(producto_id, **datos):
        """
        Actualiza un producto existente con datos proporcionados.
        Lanza una excepción ValidationError si los datos son inválidos.
        """
        producto = get_object_or_404(Producto, id=producto_id)

        # Validaciones
        if "precio_venta" in datos and datos["precio_venta"] < 0:
            raise ValidationError("El precio de venta no puede ser negativo.")
        if "stock" in datos and "stock_minimo" in datos and datos["stock"] < datos["stock_minimo"]:
            raise ValidationError("El stock no puede ser menor al stock mínimo.")
        if "fecha_caducidad" in datos and datos["fecha_caducidad"] < now().date():
            raise ValidationError("La fecha de caducidad no puede ser una fecha pasada.")

        # Actualizar atributos
        for key, value in datos.items():
            setattr(producto, key, value)
        producto.save()
        return producto

    @staticmethod
    def eliminar_producto(producto_id):
        """
        Marca un producto como inactivo.
        """
        producto = get_object_or_404(Producto, id=producto_id)
        producto.activo = False
        producto.save()
        return producto

    @staticmethod
    def productos_por_fecha_caducidad(fecha):
        """
        Devuelve productos que caducan antes de una fecha específica.
        Solo incluye productos activos.
        """
        return Producto.objects.filter(fecha_caducidad__lte=fecha, activo=True)
