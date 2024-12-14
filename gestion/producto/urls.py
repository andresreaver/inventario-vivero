from django.urls import path

from gestion.compra import compra_views
from gestion.producto import producto_views
from gestion.producto.producto_views import crear_producto, editar_producto, eliminar_producto
from gestion.urls import urlpatterns

urlpatterns = [
    path('productos/', producto_views.lista_productos, name='lista_productos'),
    path('productos/crear/', crear_producto, name='crear_producto'),
    path('productos/editar/<int:producto_id>/', editar_producto, name='editar_producto'),
    path('productos/eliminar/<int:producto_id>/', eliminar_producto, name='eliminar_producto'),
]
