from django.shortcuts import render, redirect
from gestion.models.compra import Compra
from gestion.models.proveedor import Proveedor
from gestion.models.producto import Producto

def lista_compras(request):
    """
    Vista para listar todas las compras.
    """
    compras = Compra.objects.select_related('proveedor', 'producto').all()
    return render(request, 'compras.html', {'compras': compras})

def registrar_compra(request):
    """
    Vista para registrar una nueva compra.
    """
    if request.method == 'POST':
        proveedor_id = request.POST.get('proveedor')
        producto_id = request.POST.get('producto')
        cantidad = request.POST.get('cantidad')
        precio_unitario = request.POST.get('precio_unitario')
        numero_factura = request.POST.get('numero_factura')
        fecha = request.POST.get('fecha')

        try:
            proveedor = Proveedor.objects.get(id=proveedor_id)
            producto = Producto.objects.get(id=producto_id)

            Compra.objects.create(
                proveedor=proveedor,
                producto=producto,
                cantidad=int(cantidad),
                precio_unitario=float(precio_unitario),
                numero_factura=numero_factura,
                fecha=fecha
            )
            return redirect('compras')
        except Exception as e:
            compras = Compra.objects.select_related('proveedor', 'producto').all()
            proveedores = Proveedor.objects.all()
            productos = Producto.objects.all()
            return render(request, 'compras.html', {
                'error': str(e),
                'compras': compras,
                'proveedores': proveedores,
                'productos': productos
            })

    compras = Compra.objects.select_related('proveedor', 'producto').all()
    proveedores = Proveedor.objects.all()
    productos = Producto.objects.all()
    return render(request, 'compras.html', {
        'compras': compras,
        'proveedores': proveedores,
        'productos': productos
    })
