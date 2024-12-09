from django.shortcuts import render, redirect
from gestion.services.cliente_service import ClienteService
from django.contrib import messages

def lista_clientes(request):
    """Vista para listar clientes"""
    clientes = ClienteService.obtener_clientes()
    return render(request, 'lista_clientes.html', {'clientes': clientes})

def crear_cliente(request):
    """Vista para crear un nuevo cliente"""
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        telefono = request.POST.get('telefono')
        email = request.POST.get('email')
        direccion = request.POST.get('direccion')
        try:
            ClienteService.crear_cliente(nombre, telefono, email, direccion)
            messages.success(request, 'Cliente creado con éxito.')
        except Exception as e:
            messages.error(request, f'Error al crear cliente: {str(e)}')
        return redirect('lista_clientes')
    return render(request, 'crear_cliente.html')
