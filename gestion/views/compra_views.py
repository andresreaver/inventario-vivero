from django.shortcuts import render, redirect
from gestion.models import Proveedor, Producto
from gestion.services.compra_service import CompraService
from django.contrib import messages


def compras(request):
    if request.method == 'POST':
        proveedor_id = request.POST.get('proveedor')
        producto_id = request.POST.get('producto')
        cantidad = int(request.POST.get('cantidad', 0))
        precio_unitario = float(request.POST.get('precio_unitario', 0))

        try:
            CompraService.registrar_compra(proveedor_id, producto_id, cantidad, precio_unitario)
            messages.success(request, "Compra registrada exitosamente.")
        except ValueError as e:
            messages.error(request, str(e))
        except Exception as e:
            messages.error(request, f"Error inesperado: {str(e)}")

        return redirect('compras')

    proveedores = Proveedor.objects.all()
    productos = Producto.objects.filter(activo=True)
    compras = CompraService.obtener_compras()

    return render(request, 'compras.html', {
        'proveedores': proveedores,
        'productos': productos,
        'compras': compras
    })
