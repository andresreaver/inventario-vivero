from django.shortcuts import render, redirect
from gestion.models import Proveedor, Producto
from gestion.services.compra_service import CompraService
from django.contrib import messages

def compras(request):
    """
    Vista para manejar el registro y la visualización de compras.
    """
    if request.method == 'POST':
        # Registrar una nueva compra
        proveedor_id = request.POST.get('proveedor')
        producto_id = request.POST.get('producto')
        cantidad = int(request.POST.get('cantidad', 0))
        precio_unitario = float(request.POST.get('precio_unitario', 0))

        try:
            # Validar existencia de proveedor y producto
            proveedor = Proveedor.objects.get(id=proveedor_id)
            producto = Producto.objects.get(id=producto_id, activo=True)

            # Registrar la compra
            CompraService.registrar_compra(proveedor, producto, cantidad, precio_unitario)
            messages.success(request, "Compra registrada exitosamente.")
        except Proveedor.DoesNotExist:
            messages.error(request, "El proveedor seleccionado no existe.")
        except Producto.DoesNotExist:
            messages.error(request, "El producto seleccionado no existe o está inactivo.")
        except ValueError:
            messages.error(request, "Los datos ingresados no son válidos.")
        except Exception as e:
            messages.error(request, f"Ocurrió un error inesperado: {str(e)}")
        return redirect('compras')

    # Obtener datos para el formulario y listado
    proveedores = Proveedor.objects.all()
    productos = Producto.objects.filter(activo=True)
    compras = CompraService.obtener_compras()

    return render(request, 'compras.html', {
        'proveedores': proveedores,
        'productos': productos,
        'compras': compras
    })

def registrar_compra(request):
    """
    Vista para registrar una compra.
    """
    if request.method == 'POST':
        proveedor_id = request.POST.get('proveedor')
        producto_id = request.POST.get('producto')
        cantidad = int(request.POST.get('cantidad', 0))
        precio_unitario = float(request.POST.get('precio_unitario', 0))

        try:
            proveedor = Proveedor.objects.get(id=proveedor_id)
            producto = Producto.objects.get(id=producto_id, activo=True)
            CompraService.registrar_compra(proveedor, producto, cantidad, precio_unitario)
            messages.success(request, "Compra registrada exitosamente.")
        except Exception as e:
            messages.error(request, f"Error al registrar compra: {str(e)}")

        return redirect('registrar_compra')

    proveedores = Proveedor.objects.all()
    productos = Producto.objects.filter(activo=True)
    compras = CompraService.obtener_compras()

    return render(request, 'compras.html', {
        'proveedores': proveedores,
        'productos': productos,
        'compras': compras
    })


def lista_compras(request):
    """
    Lista todas las compras registradas.
    """
    # Usar el servicio para obtener todas las compras
    compras = CompraService.obtener_compras()

    # Renderizar la plantilla con la lista de compras
    return render(request, 'compras.html', {'compras': compras})