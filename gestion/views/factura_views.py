from django.shortcuts import render, redirect, get_object_or_404
from gestion.services.factura_service import FacturaService
from gestion.services.cliente_service import ClienteService
from gestion.services.producto_service import ProductoService
from django.contrib import messages

def lista_facturas(request):
    """Vista para listar facturas"""
    facturas = FacturaService.obtener_facturas()
    return render(request, 'lista_facturas.html', {'facturas': facturas})

def crear_factura(request):
    """Vista para crear una nueva factura"""
    if request.method == 'POST':
        cliente_id = request.POST.get('cliente')
        productos_ids = request.POST.getlist('productos')  # Lista de IDs de productos seleccionados
        cantidades = request.POST.getlist('cantidades')  # Lista de cantidades correspondientes
        total = 0

        try:
            cliente = ClienteService.obtener_clientes().get(id=cliente_id)
            factura = FacturaService.crear_factura(cliente, total)

            # Relacionar productos y calcular el total
            for producto_id, cantidad in zip(productos_ids, cantidades):
                producto = ProductoService.obtener_producto_por_id(producto_id)
                cantidad = int(cantidad)
                total += producto.precio * cantidad

                # Reducir stock en inventario
                ProductoService.actualizar_stock(producto.id, -cantidad)

            # Actualizar el total de la factura
            factura.total = total
            factura.save()

            messages.success(request, 'Factura creada con éxito.')
        except Exception as e:
            messages.error(request, f'Error al crear factura: {str(e)}')
        return redirect('lista_facturas')

    clientes = ClienteService.obtener_clientes()
    productos = ProductoService.obtener_productos()
    return render(request, 'crear_factura.html', {'clientes': clientes, 'productos': productos})

