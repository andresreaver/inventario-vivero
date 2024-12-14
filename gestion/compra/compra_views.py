from gestion.compra.compra_service import CompraService
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from gestion.compra.compra import Compra

@login_required
def compras(request):
    compras = Compra.objects.all()
    return render(request, 'compra/compras.html', {'compras': compras})


@login_required
def lista_compras(request):
    compras = CompraService.obtener_compras()
    return render(request, 'lista_compras.html', {'compras': compras})
