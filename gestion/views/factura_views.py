from django.shortcuts import render, redirect, get_object_or_404
from gestion.services.factura_service import FacturaService
from gestion.services.cliente_service import ClienteService
from gestion.services.producto_service import ProductoService
from django.contrib import messages
from django.db import transaction

def lista_facturas(request):
    """Vista para listar facturas"""
    facturas = FacturaService.obtener_facturas()
    return render(request, 'lista_facturas.html', {'facturas': facturas})

@transaction.atomic
def crear_factura(request):
    """Vista para crear una nueva factura"""
    if request.method == 'POST':
        cliente_id = request.POST.get('cliente')
        productos_ids = request.POST.getlist('productos')
        cantidades = request.POST.getlist('cantidades')

        if not cliente_id or not productos_ids or not cantidades:
            messages.error(request, 'Debe seleccionar un cliente y al menos un producto con su cantidad.')
            return redirect('crear_factura')

        if len(productos_ids) != len(cantidades):
            messages.error(request, 'Hay una inconsistencia en los productos y cantidades proporcionados.')
            return redirect('crear_factura')

        try:
            cliente = get_object_or_404(ClienteService.obtener_clientes(), id=cliente_id)

            # Crear la factura inicial con total temporal
            factura = FacturaService.crear_factura(cliente, total=0)

            total = 0
            for producto_id, cantidad in zip(productos_ids, cantidades):
                producto = ProductoService.obtener_producto_por_id(producto_id)
                cantidad = int(cantidad)

                if cantidad <= 0:
                    messages.error(request, f'La cantidad para el producto "{producto.nombre}" debe ser mayor a 0.')
                    raise ValueError("Cantidad inválida.")

                if producto.stock < cantidad:
                    messages.error(request, f'No hay suficiente stock para el producto "{producto.nombre}".')
                    raise ValueError("Stock insuficiente.")

                # Actualizar stock y calcular total
                ProductoService.actualizar_stock(producto.id, -cantidad)
                total += producto.precio * cantidad

                # Asociar producto a la factura
                FacturaService.agregar_producto_a_factura(factura, producto, cantidad)

            # Actualizar el total en la factura
            factura.total = total
            factura.save()

            messages.success(request, 'Factura creada con éxito.')
            return redirect('lista_facturas')

        except Exception as e:
            messages.error(request, f'Error al crear la factura: {str(e)}')
            transaction.set_rollback(True)
            return redirect('crear_factura')

    # Si es una petición GET, renderizar la plantilla
    clientes = ClienteService.obtener_clientes()
    productos = ProductoService.obtener_productos()
    return render(request, 'crear_factura.html', {'clientes': clientes, 'productos': productos})
