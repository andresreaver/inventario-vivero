from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from gestion.services.cliente_service import ClienteService
from django.contrib import messages

@login_required
def lista_clientes(request):
    clientes = ClienteService.obtener_clientes()
    return render(request, 'clientes/lista_clientes.html', {'clientes': clientes})

@login_required
def crear_cliente(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        cedula = request.POST['cedula']
        direccion = request.POST.get('direccion')
        telefono = request.POST.get('telefono')

        try:
            ClienteService.crear_cliente(nombre, cedula, direccion, telefono)
            messages.success(request, f"Cliente {nombre} creado con éxito.")
            return redirect('lista_clientes')
        except Exception as e:
            messages.error(request, f"Error al crear cliente: {str(e)}")

    return render(request, 'clientes/crear_cliente.html')
