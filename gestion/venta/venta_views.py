from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from gestion.venta.venta import Venta

@login_required
def ventas(request):
    ventas = Venta.objects.all()
    return render(request, 'venta/ventas.html', {'ventas': ventas})
