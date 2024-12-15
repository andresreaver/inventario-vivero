from django.shortcuts import get_object_or_404, redirect, render
from gestion.models.cliente import Cliente
from gestion.forms import ClienteForm


def listar_clientes(request):
    """
    Vista para listar todos los clientes.
    """
    clientes = Cliente.objects.all()
    return render(request, 'listar_clientes.html', {'clientes': clientes})


def crear_cliente(request):
    """
    Vista para crear un nuevo cliente.
    """
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_clientes')  # Redirige a la lista de clientes
    else:
        form = ClienteForm()
    return render(request, 'form_cliente.html', {'form': form, 'accion': 'Crear'})


def editar_cliente(request, pk):
    """
    Vista para editar un cliente existente.
    """
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('listar_clientes')  # Redirige a la lista de clientes
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'form_cliente.html', {'form': form, 'accion': 'Editar'})


def eliminar_cliente(request, pk):
    """
    Vista para eliminar un cliente.
    """
    cliente = get_object_or_404(Cliente, pk=pk)
    cliente.delete()
    return redirect('listar_clientes')
