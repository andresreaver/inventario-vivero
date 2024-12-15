from gestion.models.inventario import Producto, MovimientoInventario

def obtener_productos():
    return Producto.objects.all()

def obtener_historial_movimientos():
    return MovimientoInventario.objects.select_related('producto', 'cliente').order_by('-fecha')

def descargar_informe_csv():
    import csv
    from io import StringIO
    movimientos = obtener_historial_movimientos()
    output = StringIO()
    writer = csv.writer(output)
    writer.writerow(['Producto', 'Tipo', 'Cantidad', 'Fecha', 'Cliente', 'Tipo Pago', 'Precio Total'])
    for m in movimientos:
        writer.writerow([
            m.producto.nombre, m.tipo_movimiento, m.cantidad, m.fecha,
            m.cliente.username if m.cliente else '', m.tipo_pago, m.precio_total
        ])
    return output.getvalue()
