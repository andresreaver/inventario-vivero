from django.urls import path
from . import views
from gestion.views.user_views import admin_dashboard, logout_view
from .views import user_views, producto_views, compra_views, crear_producto, editar_producto, eliminar_producto, \
    lista_compras, compras
from .views.cliente_views import crear_cliente, listar_clientes, editar_cliente, eliminar_cliente
from .views.factura_views import lista_facturas, crear_factura
from .views.informe_views import informes
from .views.inventario_view import descargar_informe, inventario_actual, historial_movimientos
from .views.proveedor_views import listar_proveedores, crear_proveedor, editar_proveedor, eliminar_proveedor
from .views.venta_views import ventas, lista_ventas, registrar_venta


urlpatterns = [
    #Login
    path('login/', user_views.login_view, name='login'),
    path('logout/', user_views.logout_view, name='logout'),
    path('admin-dashboard/', admin_dashboard, name='admin_dashboard'),
    path('productos/', producto_views.lista_productos, name='lista_productos'),
    path('productos/crear/', crear_producto, name='crear_producto'),
    path('productos/editar/<int:producto_id>/', editar_producto, name='editar_producto'),
    path('productos/eliminar/<int:producto_id>/', eliminar_producto, name='eliminar_producto'),
    path('compras/', compras, name='compras'),
    path('password-reset/', user_views.password_reset_request, name='password_reset_request'),
    path('reset-password/<uidb64>/<token>/', user_views.password_reset, name='password_reset'),
    #path('ventas/', ventas, name='ventas'),
    path('informes/', informes, name='informes'),

    # Clientes
    path('clientes/', listar_clientes, name='listar_clientes'),
    path('clientes/crear/', crear_cliente, name='crear_cliente'),
    path('clientes/editar/<int:pk>/', editar_cliente, name='editar_cliente'),
    path('clientes/eliminar/<int:pk>/', eliminar_cliente, name='eliminar_cliente'),

    # Ventas
    path('ventas/', ventas, name='ventas'),
    path('ventas/', lista_ventas, name='lista_ventas'),
    path('ventas/registrar/', registrar_venta, name='registrar_venta'),

    # Proveedores
    path('proveedores/', listar_proveedores, name='proveedor'),
    path('proveedores/nuevo/', crear_proveedor, name='crear_proveedor'),
    path('proveedores/editar/<int:pk>/', editar_proveedor, name='editar_proveedor'),
    path('proveedores/eliminar/<int:pk>/', eliminar_proveedor, name='eliminar_proveedor'),

    # facturas
    path('facturas/', lista_facturas, name='lista_facturas'),
    # path('facturas/<int:factura_id>/', detalle_factura_view, name='detalle_factura'),
    path('facturas/crear/', crear_factura, name='crear_factura'),

    #Inventarios
    path('inventario/', inventario_actual, name='inventario_actual'),
    path('historial/', historial_movimientos, name='historial_movimientos'),
    path('descargar-informe/', descargar_informe, name='descargar_informe'),
]
