from gestion.models import CustomUser

class UserService:
    @staticmethod
    def crear_usuario(username, email, password, role='user', is_superuser=False, is_staff=False):
        """Crea un nuevo usuario en el sistema."""
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

    @staticmethod
    def obtener_usuarios():
        """Devuelve una lista de todos los usuarios."""
        return CustomUser.objects.all()

    @staticmethod
    def actualizar_usuario(user_id, **kwargs):
        """Actualiza un usuario existente."""
        user = CustomUser.objects.get(id=user_id)
        for key, value in kwargs.items():
            setattr(user, key, value)
        user.save()
        return user

    @staticmethod
    def eliminar_usuario(user_id):
        """Elimina un usuario del sistema."""
        user = CustomUser.objects.get(id=user_id)
        user.delete()
