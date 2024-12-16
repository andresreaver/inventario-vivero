from django.shortcuts import render, redirect
from gestion.models import *
from gestion.services.compra_service import CompraService


def compras(request):
    if request.method == 'POST':
        proveedor_id = request.POST['proveedor']
        producto_id = request.POST['producto']
        cantidad = int(request.POST['cantidad'])
        precio_unitario = float(request.POST['precio_unitario'])

        try:
            CompraService.registrar_compra(proveedor_id, producto_id, cantidad, precio_unitario)
        except ValueError as e:
            return render(request, 'compras.html', {
                'error': str(e),
                'proveedores': Proveedor.objects.all(),
                'productos': Producto.objects.all(),
                'compras': CompraService.obtener_compras()
            })

        return redirect('compras')

    return render(request, 'compras.html', {
        'proveedores': Proveedor.objects.all(),
        'productos': Producto.objects.all(),
        'compras': CompraService.obtener_compras()
    })
def lista_compras(request):
    """
    Vista para listar todas las compras.
    """
    compras = Compra.objects.all()  # Consulta todas las compras
    return render(request, 'compras.html', {'compras': compras})