from django.urls import path
from . import views
from .views import user_views, producto_views, compra_views

urlpatterns = [
    path('login/', user_views.login_view, name='login'),
    path('logout/', user_views.logout_view, name='logout'),
    path('admin-dashboard/', user_views.admin_dashboard, name='admin_dashboard'),
    path('productos/', producto_views.lista_productos, name='lista_productos'),
    path('compras/', compra_views.lista_compras, name='lista_compras'),
    path('password-reset/', user_views.password_reset_request, name='password_reset_request'),
    path('reset-password/<uidb64>/<token>/', user_views.password_reset, name='password_reset'),

]
