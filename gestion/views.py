from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import authenticate, login, get_user_model
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from gestion.models import Producto

# Obtener el modelo de usuario personalizado
CustomUser = get_user_model()

# Decorador para verificar superusuario
def superuser_required(view_func):
    return user_passes_test(lambda user: user.is_superuser)(view_func)

# Vista: Lista de productos (usuarios normales)
@login_required
def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, "lista_productos.html", {"productos": productos})

# Vista: Panel de administración
@superuser_required
def admin_dashboard(request):
    if request.method == 'POST':
        if 'create_user' in request.POST:  # Crear un usuario
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            role = request.POST.get('role')
            is_staff = 'is_staff' in request.POST
            is_superuser = 'is_superuser' in request.POST

            if CustomUser.objects.filter(username=username).exists():
                messages.error(request, f"El usuario {username} ya existe.")
            else:
                try:
                    user = CustomUser.objects.create_user(
                        username=username,
                        email=email,
                        password=password,
                    )
                    user.role = role
                    user.is_staff = is_staff
                    user.is_superuser = is_superuser
                    user.save()
                    messages.success(request, f"Usuario {username} creado con éxito.")
                except Exception as e:
                    messages.error(request, f"Error al crear el usuario: {str(e)}")

        elif 'delete_user' in request.POST:  # Eliminar un usuario
            user_id = request.POST.get('user_id')
            user = get_object_or_404(CustomUser, id=user_id)
            user.delete()
            messages.success(request, f"Usuario eliminado con éxito.")

        elif 'update_user' in request.POST:  # Actualizar un usuario
            user_id = request.POST.get('user_id')
            user = get_object_or_404(CustomUser, id=user_id)
            user.role = request.POST.get('role')
            user.is_staff = 'is_staff' in request.POST
            user.is_superuser = 'is_superuser' in request.POST
            user.save()
            messages.success(request, f"Usuario {user.username} actualizado con éxito.")

    users = CustomUser.objects.all()
    return render(request, 'admin_dashboard.html', {'users': users})

# Vista: Login
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            if user.is_superuser:
                return redirect('admin_dashboard')
            else:
                return redirect('lista_productos')
        else:
            messages.error(request, 'Credenciales inválidas. Inténtalo de nuevo.')
    return render(request, 'login.html')

@superuser_required
def manage_users(request):
    users = CustomUser.objects.all()
    return render(request, 'manage_users.html', {'users': users})

@user_passes_test(lambda user: user.is_superuser)
def edit_user(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    if request.method == 'POST':
        user.username = request.POST.get('username')
        user.email = request.POST.get('email')
        user.role = request.POST.get('role')
        user.is_staff = 'is_staff' in request.POST
        user.is_superuser = 'is_superuser' in request.POST
        user.save()
        messages.success(request, f"Usuario {user.username} actualizado con éxito.")
        return redirect('manage_users')
    return render(request, 'edit_user.html', {'user': user})

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from gestion.models import Cliente  # Importa el modelo de clientes

@login_required
def lista_clientes(request):
    clientes = Cliente.objects.all()  # Recupera todos los clientes
    return render(request, "cliente.html", {"clientes": clientes})  # Usa la plantilla existente
