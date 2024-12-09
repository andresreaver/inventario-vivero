from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib import messages
from gestion.services.user_service import UserService

CustomUser = get_user_model()


# -------------------------------------
# Función para validar superusuario
# -------------------------------------
def is_superuser(user):
    return user.is_superuser


# -------------------------------------
# Vista para el Admin Dashboard
# -------------------------------------
@login_required
@user_passes_test(is_superuser)
def admin_dashboard(request):
    if request.method == 'POST':
        if 'create_user' in request.POST:  # Crear un nuevo usuario
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            role = request.POST.get('role')
            is_staff = 'is_staff' in request.POST
            is_superuser = 'is_superuser' in request.POST

            try:
                UserService.crear_usuario(username, email, password, role, is_superuser, is_staff)
                messages.success(request, f"Usuario {username} creado con éxito.")
            except Exception as e:
                messages.error(request, f"Error al crear usuario: {str(e)}")

        elif 'update_user' in request.POST:  # Actualizar usuario existente
            user_id = request.POST.get('user_id')
            role = request.POST.get('role')
            is_staff = 'is_staff' in request.POST
            is_superuser = 'is_superuser' in request.POST
            try:
                UserService.actualizar_usuario(user_id, role, is_superuser, is_staff)
                messages.success(request, f"Usuario actualizado con éxito.")
            except Exception as e:
                messages.error(request, f"Error al actualizar usuario: {str(e)}")

        elif 'delete_user' in request.POST:  # Eliminar usuario
            user_id = request.POST.get('user_id')
            try:
                UserService.eliminar_usuario(user_id)
                messages.success(request, f"Usuario eliminado con éxito.")
            except Exception as e:
                messages.error(request, f"Error al eliminar usuario: {str(e)}")

    users = UserService.obtener_usuarios()
    return render(request, 'admin_dashboard.html', {'users': users})


# -------------------------------------
# Vista para Login
# -------------------------------------
def login_view(request):
    """Vista para iniciar sesión"""
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_superuser:
                return redirect('admin_dashboard')  # Redirige al administrador
            return redirect('lista_productos')  # Redirige a usuarios normales
        else:
            messages.error(request, 'Credenciales inválidas. Inténtalo de nuevo.')
    return render(request, 'login.html')


# -------------------------------------
# Vista para Logout
# -------------------------------------
def logout_view(request):
    """Cerrar sesión"""
    logout(request)
    return redirect('login')


# -------------------------------------
# Vista para Solicitar Restablecimiento de Contraseña
# -------------------------------------
def password_reset_request(request):
    if request.method == 'POST':
        email = request.POST['email']
        try:
            user = CustomUser.objects.get(email=email)
            token = default_token_generator.make_token(user)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            reset_url = request.build_absolute_uri(f"/reset-password/{uid}/{token}/")
            subject = 'Restablecimiento de contraseña'
            message = render_to_string('password_reset_email.html', {'reset_url': reset_url})
            send_mail(subject, message, 'tu_correo@gmail.com', [email])
            return render(request, 'password_reset_done.html')  # Página de confirmación
        except CustomUser.DoesNotExist:
            return render(request, 'password_reset_request.html', {'error': 'Correo no registrado.'})
    return render(request, 'password_reset_request.html')


# -------------------------------------
# Vista para Restablecer Contraseña
# -------------------------------------
def password_reset(request, uidb64, token):
    if request.method == 'POST':
        password = request.POST['password']
        user_id = force_bytes(urlsafe_base64_decode(uidb64))
        user = get_object_or_404(CustomUser, pk=user_id)
        if default_token_generator.check_token(user, token):
            user.set_password(password)
            user.save()
            messages.success(request, 'Contraseña restablecida con éxito.')
            return redirect('login')
        else:
            return render(request, 'password_reset_invalid.html')
    return render(request, 'password_reset_form.html', {'uidb64': uidb64, 'token': token})
