from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from xhtml2pdf import pisa
from gestion.models import Venta

def informe_ventas(request):
    """Muestra el informe de ventas."""
    ventas = Venta.objects.all()
    total_ventas = sum(venta.cantidad * venta.precio_unitario for venta in ventas)

    context = {
        'ventas': ventas,
        'total_ventas': total_ventas,
    }
    return render(request, 'reports/ventas_dashboard.html', context)

def informe_ventas_pdf(request):
    """Genera un PDF del informe de ventas."""
    ventas = Venta.objects.all()
    total_ventas = sum(venta.cantidad * venta.precio_unitario for venta in ventas)

    context = {
        'ventas': ventas,
        'total_ventas': total_ventas,
    }
    html = render_to_string('reports/ventas_pdf.html', context)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="informe_ventas.pdf"'
    pisa_status = pisa.CreatePDF(html, dest=response)

    if pisa_status.err:
        return HttpResponse("Error al generar el PDF", status=500)
    return response
