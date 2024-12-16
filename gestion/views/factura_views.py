from django.shortcuts import render, redirect, get_object_or_404
from gestion.services.cliente_service import ClienteService
from gestion.services.producto_service import ProductoService
from gestion.services.factura_service import FacturaService
from django.contrib import messages

def crear_factura(request):
    if request.method == 'POST':
        cliente_id = request.POST.get('cliente')
        forma_pago = request.POST.get('forma_pago')
        productos_ids = request.POST.getlist('producto[]')
        cantidades = request.POST.getlist('cantidad[]')

        try:
            cliente = ClienteService.obtener_clientes().get(id=cliente_id)

            # Preparar detalles
            detalles = []
            for producto_id, cantidad in zip(productos_ids, cantidades):
                producto = ProductoService.obtener_productos().get(id=producto_id)
                detalles.append({'producto': producto, 'cantidad': int(cantidad)})

            # Crear la factura
            FacturaService.crear_factura(cliente, forma_pago, detalles)
            messages.success(request, "Factura creada exitosamente.")
            return redirect('lista_facturas')

        except Exception as e:
            messages.error(request, f"Error al crear la factura: {str(e)}")

    clientes = ClienteService.obtener_clientes()
    productos = ProductoService.obtener_productos()
    return render(request, 'crear_factura.html', {'clientes': clientes, 'productos': productos})

def lista_facturas(request):
    """
    Vista para listar todas las facturas registradas.
    """
    try:
        # Obtener todas las facturas utilizando el servicio
        facturas = FacturaService.obtener_facturas()
        return render(request, 'lista_facturas.html', {'facturas': facturas})
    except Exception as e:
        # Manejar errores en la consulta de facturas
        return render(request, 'lista_facturas.html', {'error': f"Error al obtener las facturas: {str(e)}"})