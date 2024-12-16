from gestion.models import Producto, Venta, Compra
from datetime import date, timedelta

def obtener_inventario():
    """Obtiene los productos y los que tienen bajo stock."""
    productos = Producto.objects.all()
    productos_bajo_stock = [producto for producto in productos if producto.stock_bajo()]
    return productos, productos_bajo_stock

def obtener_ventas():
    """Obtiene todas las ventas y calcula el total generado."""
    ventas = Venta.objects.all()
    total_ventas = sum(venta.cantidad * venta.precio_unitario for venta in ventas)
    return ventas, total_ventas

def obtener_compras():
    """Obtiene todas las compras y calcula el total gastado."""
    compras = Compra.objects.all()
    total_compras = sum(compra.cantidad * compra.precio_unitario for compra in compras)
    return compras, total_compras

def productos_proximos_a_vencer():
    """Obtiene productos cuya fecha de caducidad está cerca."""
    proximos_a_vencer = Producto.objects.filter(fecha_caducidad__lte=date.today() + timedelta(days=30))
    return proximos_a_vencer
