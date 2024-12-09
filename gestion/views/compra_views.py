from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from gestion.services.compra_service import CompraService

@login_required
def lista_compras(request):
    compras = CompraService.obtener_compras()
    return render(request, 'lista_compras.html', {'compras': compras})
