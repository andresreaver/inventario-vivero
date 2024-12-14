from django.urls import path, include

urlpatterns = [

    path('producto/', include('gestion.producto.urls')),
    path('proveedor/', include('gestion.proveedor.urls')),
    path('compra/', include('gestion.compra.urls')),
    path('venta/', include('gestion.venta.urls')),
    path('factura/', include('gestion.factura.urls')),
    path('cliente/', include('gestion.cliente.urls')),
    path('materiaprima/', include('gestion.materiaprima.urls')),
    path('user/', include('gestion.user.urls')),

]
