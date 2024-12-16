from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from gestion.services.venta_service import VentaService
from gestion.services.cliente_service import ClienteService
from gestion.services.producto_service import ProductoService
from django.contrib import messages




@login_required
def registrar_venta(request):
    clientes = ClienteService.obtener_clientes()
    productos = ProductoService.obtener_productos()

    if request.method == 'POST':
        cliente_id = request.POST['cliente']
        producto_id = request.POST['producto']
        cantidad = int(request.POST['cantidad'])

        try:
            cliente = ClienteService.obtener_cliente_por_id(cliente_id)
            producto = ProductoService.obtener_producto_por_id(producto_id)
            VentaService.registrar_venta(cliente, producto, cantidad)
            messages.success(request, "Venta registrada correctamente.")
            return redirect('lista_ventas')
        except Exception as e:
            messages.error(request, f"Error al registrar venta: {str(e)}")

    return render(request, 'registrar_venta.html', {'clientes': clientes, 'productos': productos})

@login_required
def lista_ventas(request):
    ventas = VentaService.obtener_ventas()
    return render(request, 'ventas.html', {'ventas': ventas})


@login_required
def ventas(request):
    return render(request, 'ventas.html')