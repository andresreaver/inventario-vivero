from django.urls import path

from gestion.compra import compra_views
from gestion.urls import urlpatterns



urlpatterns = [
    path('compras/', compra_views.lista_compras, name='lista_compras'),
]
