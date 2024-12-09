from django.shortcuts import render, redirect
from gestion.services.proveedor_service import ProveedorService

def lista_proveedores(request):
    proveedores = ProveedorService.obtener_proveedores()
    return render(request, 'lista_proveedores.html', {'proveedores': proveedores})
