from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from gestion.services.producto_service import ProductoService
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.utils.timezone import now
from datetime import datetime


@login_required
def lista_productos(request):
    """
    Muestra una lista de productos. Solo muestra productos activos por defecto.
    """
    productos = ProductoService.obtener_productos(activos=True)
    return render(request, 'lista_productos.html', {'productos': productos})


@login_required
def crear_producto(request):
    """
    Vista para crear un nuevo producto. Valida los datos antes de crearlo.
    """
    if request.method == 'POST':
        # Obtener datos del formulario con valores por defecto
        nombre = request.POST.get('nombre', '').strip()
        tipo = request.POST.get('tipo', '').strip()
        stock = int(request.POST.get('stock', 0))
        stock_minimo = int(request.POST.get('stock_minimo', 0))
        precio_compra = request.POST.get('precio_compra', None)
        precio_venta = float(request.POST.get('precio_venta', 0))
        activo = request.POST.get('activo', 'True') == 'True'
        fecha_caducidad = request.POST.get('fecha_caducidad', None)

        # Validar precio_compra si se incluye
        if precio_compra:
            precio_compra = float(precio_compra)
            if precio_compra < 0:
                messages.error(request, "El precio de compra no puede ser negativo.")
                return render(request, 'crear_producto.html')

        # Validar fecha de caducidad
        if fecha_caducidad:
            try:
                fecha_caducidad = datetime.strptime(fecha_caducidad, '%Y-%m-%d').date()
                if fecha_caducidad < now().date():
                    messages.error(request, "La fecha de caducidad no puede ser en el pasado.")
                    return render(request, 'crear_producto.html')
            except ValueError:
                messages.error(request, "Formato de fecha inválido. Use el formato YYYY-MM-DD.")
                return render(request, 'crear_producto.html')

        try:
            # Intentar crear el producto usando el servicio
            ProductoService.crear_producto(
                nombre=nombre,
                tipo=tipo,
                stock=stock,
                stock_minimo=stock_minimo,
                precio_compra=precio_compra,
                precio_venta=precio_venta,
                fecha_caducidad=fecha_caducidad,
                activo=activo
            )
            messages.success(request, f"Producto '{nombre}' creado exitosamente.")
            return redirect('lista_productos')
        except ValidationError as e:
            messages.error(request, f"Error al crear producto: {e.message}")
        except Exception as e:
            messages.error(request, f"Ocurrió un error inesperado: {str(e)}")

    return render(request, 'crear_producto.html')


@login_required
def editar_producto(request, producto_id):
    """
    Vista para editar un producto existente. Valida los datos antes de actualizarlo.
    """
    producto = ProductoService.obtener_producto_por_id(producto_id)

    if request.method == 'POST':
        # Obtener datos del formulario
        datos = {
            'nombre': request.POST.get('nombre', producto.nombre).strip(),
            'tipo': request.POST.get('tipo', producto.tipo).strip(),
            'stock': int(request.POST.get('stock', producto.stock)),
            'stock_minimo': int(request.POST.get('stock_minimo', producto.stock_minimo)),
            'precio_compra': request.POST.get('precio_compra', producto.precio_compra),
            'precio_venta': float(request.POST.get('precio_venta', producto.precio_venta)),
            'activo': request.POST.get('activo', 'True') == 'True',
            'fecha_caducidad': request.POST.get('fecha_caducidad', producto.fecha_caducidad)
        }

        # Validar precio_compra si se incluye
        if datos['precio_compra']:
            datos['precio_compra'] = float(datos['precio_compra'])
            if datos['precio_compra'] < 0:
                messages.error(request, "El precio de compra no puede ser negativo.")
                return render(request, 'editar_producto.html', {'producto': producto})

        # Validar fecha de caducidad
        if datos['fecha_caducidad']:
            try:
                datos['fecha_caducidad'] = datetime.strptime(datos['fecha_caducidad'], '%Y-%m-%d').date()
                if datos['fecha_caducidad'] < now().date():
                    messages.error(request, "La fecha de caducidad no puede ser en el pasado.")
                    return render(request, 'editar_producto.html', {'producto': producto})
            except ValueError:
                messages.error(request, "Formato de fecha inválido. Use el formato YYYY-MM-DD.")
                return render(request, 'editar_producto.html', {'producto': producto})

        try:
            # Intentar actualizar el producto usando el servicio
            ProductoService.actualizar_producto(producto_id, **datos)
            messages.success(request, f"Producto '{datos['nombre']}' actualizado correctamente.")
            return redirect('lista_productos')
        except ValidationError as e:
            messages.error(request, f"Error al actualizar producto: {e.message}")
        except Exception as e:
            messages.error(request, f"Ocurrió un error inesperado: {str(e)}")

    return render(request, 'editar_producto.html', {'producto': producto})


@login_required
def eliminar_producto(request, producto_id):
    """
    Vista para eliminar (desactivar) un producto.
    """
    producto = ProductoService.obtener_producto_por_id(producto_id)

    if request.method == 'POST':
        try:
            # Intentar desactivar el producto usando el servicio
            ProductoService.eliminar_producto(producto_id)
            messages.success(request, f"Producto '{producto.nombre}' desactivado correctamente.")
            return redirect('lista_productos')
        except Exception as e:
            messages.error(request, f"Ocurrió un error al desactivar el producto: {str(e)}")

    return render(request, 'eliminar_producto.html', {'producto': producto})
