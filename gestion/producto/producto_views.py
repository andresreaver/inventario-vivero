from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from gestion.producto.producto_service import ProductoService
from django.contrib import messages

@login_required
def lista_productos(request):
    productos = ProductoService.obtener_productos()
    return render(request, 'producto/lista_productos.html', {'productos': productos})

@login_required
def crear_producto(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        tipo = request.POST['tipo']
        stock = int(request.POST['stock'])
        stock_minimo = int(request.POST['stock_minimo'])
        fecha_caducidad = request.POST.get('fecha_caducidad', None)

        try:
            ProductoService.crear_producto(nombre, tipo, stock, stock_minimo, fecha_caducidad)
            messages.success(request, f"Producto {nombre} creado exitosamente.")
            return redirect('lista_productos')
        except Exception as e:
            messages.error(request, f"Error al crear producto: {str(e)}")

    return render(request, 'producto/crear_producto.html')

@login_required
def editar_producto(request, producto_id):
    producto = ProductoService.obtener_producto_por_id(producto_id)
    if request.method == 'POST':
        datos = {
            'nombre': request.POST['nombre'],
            'tipo': request.POST['tipo'],
            'stock': int(request.POST['stock']),
            'stock_minimo': int(request.POST['stock_minimo']),
            'fecha_caducidad': request.POST.get('fecha_caducidad', None)
        }

        try:
            ProductoService.actualizar_producto(producto_id, **datos)
            messages.success(request, f"Producto {datos['nombre']} actualizado correctamente.")
            return redirect('lista_productos')
        except Exception as e:
            messages.error(request, f"Error al actualizar producto: {str(e)}")

    return render(request, 'producto/editar_producto.html', {'producto': producto})

@login_required
def eliminar_producto(request, producto_id):
    producto = get_object_or_404(ProductoService.obtener_productos(), id=producto_id)
    if request.method == 'POST':
        try:
            ProductoService.eliminar_producto(producto_id)
            messages.success(request, f"Producto {producto.nombre} eliminado correctamente.")
            return redirect('lista_productos')
        except Exception as e:
            messages.error(request, f"Error al eliminar producto: {str(e)}")

    return render(request, 'producto/eliminar_producto.html', {'producto': producto})
