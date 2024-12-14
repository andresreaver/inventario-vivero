from django.urls import path
from . import views
from gestion.views.user_views import admin_dashboard, logout_view
from .views import user_views, producto_views, compra_views, compras, crear_producto, editar_producto, eliminar_producto
from .views.cliente_views import lista_clientes, crear_cliente
from .views.informe_views import informes
from .views.proveedor_views import listar_proveedores, crear_proveedor, editar_proveedor, eliminar_proveedor
from .views.venta_views import ventas,  lista_ventas, registrar_venta

urlpatterns = [
    path('login/', user_views.login_view, name='login'),
    path('logout/', user_views.logout_view, name='logout'),
    path('admin-dashboard/', admin_dashboard, name='admin_dashboard'),
    path('productos/', producto_views.lista_productos, name='lista_productos'),
    path('productos/crear/', crear_producto, name='crear_producto'),
    path('productos/editar/<int:producto_id>/', editar_producto, name='editar_producto'),
    path('productos/eliminar/<int:producto_id>/', eliminar_producto, name='eliminar_producto'),
    path('compras/', compra_views.lista_compras, name='lista_compras'),
    path('password-reset/', user_views.password_reset_request, name='password_reset_request'),
    path('reset-password/<uidb64>/<token>/', user_views.password_reset, name='password_reset'),
    path('compras/', compras, name='compras'),
    path('ventas/', ventas, name='ventas'),
    path('informes/', informes, name='informes'),

# Clientes
    path('clientes/', lista_clientes, name='lista_clientes'),
    path('clientes/crear/', crear_cliente, name='crear_cliente'),

    # Ventas
    path('ventas/', ventas, name='ventas'),
    path('ventas/', lista_ventas, name='lista_ventas'),
    path('ventas/registrar/', registrar_venta, name='registrar_venta'),

    # Proveedores
    path('proveedores/', listar_proveedores, name='proveedor'),
    path('proveedores/nuevo/', crear_proveedor, name='crear_proveedor'),
    path('proveedores/editar/<int:pk>/', editar_proveedor, name='editar_proveedor'),
    path('proveedores/eliminar/<int:pk>/', eliminar_proveedor, name='eliminar_proveedor'),


]
