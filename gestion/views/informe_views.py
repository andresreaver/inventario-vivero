from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def informes(request):
    # Generar datos de informes (puedes personalizar según sea necesario)
    context = {
        'total_compras': 100,
        'total_ventas': 120,
        'productos_bajo_stock': 5,
    }
    return render(request, 'informes.html', context)
