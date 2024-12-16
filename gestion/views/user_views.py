from django.contrib.auth.decorators import login_required, user_passes_test
from gestion.services.user_service import UserService
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
from django.utils.http import urlsafe_base64_decode
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages



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
        try:
            if 'create_user' in request.POST:
                username = request.POST.get('username')
                email = request.POST.get('email')
                password = request.POST.get('password')
                role = request.POST.get('role')
                is_staff = 'is_staff' in request.POST
                is_superuser = 'is_superuser' in request.POST

                UserService.crear_usuario(username, email, password, role, is_superuser, is_staff)
                messages.success(request, f"Usuario '{username}' creado con éxito.")

            elif 'update_user' in request.POST:
                user_id = request.POST.get('user_id')
                role = request.POST.get('role')
                is_staff = 'is_staff' in request.POST
                is_superuser = 'is_superuser' in request.POST

                UserService.actualizar_usuario(user_id, role, is_superuser, is_staff)
                messages.success(request, "Usuario actualizado con éxito.")

            elif 'delete_user' in request.POST:
                user_id = request.POST.get('user_id')
                UserService.eliminar_usuario(user_id)
                messages.success(request, "Usuario eliminado con éxito.")
        except ValueError as e:
            messages.error(request, str(e))
        except Exception as e:
            messages.error(request, f"Error inesperado: {str(e)}")

    users = UserService.obtener_usuarios()
    return render(request, 'admin_dashboard.html', {'users': users})

def logout_view(request):
    """Cerrar sesión"""
    logout(request)
    return redirect('login')



def login_view(request):
    """Vista para iniciar sesión"""
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirigir según el rol del usuario
            if user.is_superuser:
                return redirect('admin_dashboard')
            else:
                return redirect('lista_productos')
        else:
            messages.error(request, 'Credenciales inválidas. Inténtalo de nuevo.')
    return render(request, 'login.html')


from django.core.mail import send_mail
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.shortcuts import render
from gestion.models import CustomUser


def password_reset_request(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            user = CustomUser.objects.get(email=email)
            token = default_token_generator.make_token(user)
            uid = urlsafe_base64_encode(user.pk)
            reset_url = request.build_absolute_uri(f"/reset-password/{uid}/{token}/")
            send_mail(
                'Restablecimiento de contraseña',
                f'Por favor haz clic en el siguiente enlace para restablecer tu contraseña: {reset_url}',
                'tuemail@example.com',
                [email],
            )
            return render(request, 'password_reset_done.html')
        except CustomUser.DoesNotExist:
            return render(request, 'password_reset_request.html', {'error': 'Correo no registrado.'})
    return render(request, 'password_reset_request.html')

def password_reset(request, uidb64, token):
    """
    Vista para restablecer la contraseña.
    """
    if request.method == 'POST':
        password = request.POST.get('password')
        try:
            user_id = urlsafe_base64_decode(uidb64).decode()
            user = get_object_or_404(CustomUser, pk=user_id)
            if default_token_generator.check_token(user, token):
                user.set_password(password)
                user.save()
                messages.success(request, 'Contraseña restablecida con éxito.')
                return redirect('login')
            else:
                messages.error(request, 'El enlace para restablecer la contraseña no es válido.')
        except Exception as e:
            messages.error(request, 'Ocurrió un error. Intenta nuevamente.')
    return render(request, 'password_reset_form.html', {'uidb64': uidb64, 'token': token})