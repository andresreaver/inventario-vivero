from django.urls import path
from . import views
from gestion.views.user_views import admin_dashboard, logout_view
from .views import user_views, producto_views, compra_views, compras
from .views.informe_views import informes
from .views.venta_views import ventas

urlpatterns = [
    path('login/', user_views.login_view, name='login'),
    path('logout/', user_views.logout_view, name='logout'),
    path('admin-dashboard/', admin_dashboard, name='admin_dashboard'),
    path('productos/', producto_views.lista_productos, name='lista_productos'),
    path('compras/', compra_views.lista_compras, name='lista_compras'),
    path('password-reset/', user_views.password_reset_request, name='password_reset_request'),
    path('reset-password/<uidb64>/<token>/', user_views.password_reset, name='password_reset'),
    path('compras/', compras, name='compras'),
    path('ventas/', ventas, name='ventas'),
    path('informes/', informes, name='informes'),

]
