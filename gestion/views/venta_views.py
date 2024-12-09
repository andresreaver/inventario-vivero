from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from gestion.models.venta import Venta

@login_required
def ventas(request):
    ventas = Venta.objects.all()
    return render(request, 'ventas.html', {'ventas': ventas})
