from django.urls import path
from gestion.views.user_views import admin_dashboard
from .views import user_views, producto_views, compra_views
from .views.informe_views import informes
from .views.venta_views import ventas

from gestion.views.proveedor_views import (
    listar_proveedores,
    crear_proveedor,
    editar_proveedor,
    eliminar_proveedor,
)
from gestion.views.cliente_views import (
    listar_clientes,
    crear_cliente,
    editar_cliente,
    eliminar_cliente,
)

from gestion.views.compra_views import (
    lista_compras,
    registrar_compra,

)

urlpatterns = [
    path('login/', user_views.login_view, name='login'),
    path('logout/', user_views.logout_view, name='logout'),
    path('admin-dashboard/', admin_dashboard, name='admin_dashboard'),
    path('productos/', producto_views.lista_productos, name='lista_productos'),
    path('password-reset/', user_views.password_reset_request, name='password_reset_request'),
    path('reset-password/<uidb64>/<token>/', user_views.password_reset, name='password_reset'),
    path('compras/', lista_compras, name='compras'),
    path('compras/registrar/', registrar_compra, name='registrar_compra'),
    path('ventas/', ventas, name='ventas'),
    path('informes/', informes, name='informes'),
    path('proveedores/', listar_proveedores, name='proveedor'),
    path('proveedores/nuevo/', crear_proveedor, name='crear_proveedor'),
    path('proveedores/editar/<int:pk>/', editar_proveedor, name='editar_proveedor'),
    path('proveedores/eliminar/<int:pk>/', eliminar_proveedor, name='eliminar_proveedor'),
    path('clientes/', listar_clientes, name='cliente'),
    path('clientes/nuevo/', crear_cliente, name='crear_cliente'),
    path('clientes/editar/<int:pk>/', editar_cliente, name='editar_cliente'),
    path('clientes/eliminar/<int:pk>/', eliminar_cliente, name='eliminar_cliente'),
]


