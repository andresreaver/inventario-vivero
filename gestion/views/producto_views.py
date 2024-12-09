from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from gestion.services.producto_service import ProductoService

@login_required
def lista_productos(request):
    productos = ProductoService.obtener_productos()
    return render(request, 'lista_productos.html', {'productos': productos})
