from django.shortcuts import get_object_or_404, redirect, render
from gestion.models.proveedor import Proveedor
from gestion.forms import ProveedorForm


def listar_proveedores(request):
    proveedores = Proveedor.objects.all()
    return render(request, 'proveedor.html', {'proveedores': proveedores})

def editar_proveedor(request, pk):
    proveedor = get_object_or_404(Proveedor, pk=pk)
    if request.method == 'POST':
        form = ProveedorForm(request.POST, instance=proveedor)
        if form.is_valid():
            form.save()
            return redirect('proveedor')  # Alias corregido
    else:
        form = ProveedorForm(instance=proveedor)
    return render(request, 'proveedor.html', {'form': form})


def crear_proveedor(request):
    from gestion.forms import ProveedorForm  # Asegúrate de importar el formulario correctamente
    if request.method == 'POST':
        form = ProveedorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('proveedor')  # Alias corregido
    else:
        form = ProveedorForm()
    return render(request, 'proveedor.html', {'form': form})


def eliminar_proveedor(request, pk):
    proveedor = get_object_or_404(Proveedor, pk=pk)
    proveedor.delete()
    return redirect('proveedor')  # Cambia el nombre por el alias de tu URL para listar proveedores