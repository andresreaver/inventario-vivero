from gestion.models import CustomUser


class UserService:
    @staticmethod
    def crear_usuario(username, email, password, role='user', is_superuser=False, is_staff=False):
        """Crea un nuevo usuario en el sistema."""
        try:
            user = CustomUser.objects.create_user(
                username=username,
                email=email,
                password=password
            )
            user.role = role
            user.is_superuser = is_superuser
            user.is_staff = is_staff
            user.save()
            return user
        except Exception as e:
            raise ValueError(f"Error al crear el usuario: {str(e)}")

    @staticmethod
    def obtener_usuarios():
        """Devuelve una lista de todos los usuarios."""
        return CustomUser.objects.all()

    @staticmethod
    def actualizar_usuario(user_id, role=None, is_superuser=False, is_staff=False):
        """Actualiza un usuario existente."""
        try:
            user = CustomUser.objects.get(id=user_id)
            if role:
                user.role = role
            user.is_superuser = bool(is_superuser)
            user.is_staff = bool(is_staff)
            user.save()
            return user
        except CustomUser.DoesNotExist:
            raise ValueError("El usuario no existe.")
        except Exception as e:
            raise ValueError(f"Error al actualizar el usuario: {str(e)}")

    @staticmethod
    def eliminar_usuario(user_id):
        """Elimina un usuario del sistema."""
        try:
            user = CustomUser.objects.get(id=user_id)
            user.delete()
        except CustomUser.DoesNotExist:
            raise ValueError("El usuario no existe.")
