from django.urls import path

from gestion.compra import compra_views
from gestion.urls import urlpatterns
from gestion.user import user_views
from gestion.user.user_views import admin_dashboard

urlpatterns = [

    path('login/', user_views.login_view, name='login'),
    path('logout/', user_views.logout_view, name='logout'),
    path('admin-dashboard/', admin_dashboard, name='admin_dashboard'),
    path('password-reset/', user_views.password_reset_request, name='password_reset_request'),
    path('reset-password/<uidb64>/<token>/', user_views.password_reset, name='password_reset'),

]