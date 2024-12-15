from django.shortcuts import render, HttpResponse
from gestion.services.inventario_service import obtener_productos, obtener_historial_movimientos, descargar_informe_csv

def inventario_actual(request):
    productos = obtener_productos()
    return render(request, 'gestion/inventario_actual.html', {'productos': productos})

def historial_movimientos(request):
    movimientos = obtener_historial_movimientos()
    return render(request, 'gestion/historial_movimientos.html', {'movimientos': movimientos})

def descargar_informe(request):
    csv_data = descargar_informe_csv()
    response = HttpResponse(csv_data, content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="movimientos_inventario.csv"'
    return response
