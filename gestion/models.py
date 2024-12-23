# from django.db import models
# from django.contrib.auth.models import AbstractUser
#
# class CustomUser(AbstractUser):
#     ROLE_CHOICES = (
#         ('admin', 'Administrador'),
#         ('user', 'Usuario'),
#     )
#     role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='user')
#
# class Proveedor(models.Model):
#     nombre = models.CharField(max_length=200, unique=True)
#     telefono = models.CharField(max_length=15, blank=True, null=True)
#     email = models.EmailField(blank=True, null=True)
#
#     def __str__(self):
#         return self.nombre
#
# class Compra(models.Model):
#     proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE, related_name='compras')
#     producto = models.ForeignKey('Producto', on_delete = models.CASCADE)
#     cantidad = models.PositiveIntegerField()
#     fecha = models.DateTimeField(auto_now_add=True)
#     precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
#
#     def __str__(self):
#         return f"{self.producto.nombre} - {self.cantidad} unidades"
#
# class Venta(models.Model):
#     producto = models.ForeignKey('Producto', on_delete=models.CASCADE)
#     cantidad = models.PositiveIntegerField()
#     fecha = models.DateTimeField(auto_now_add=True)
#     precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
#
#     def __str__(self):
#         return f"Venta de {self.producto.nombre} - {self.cantidad} unidades"
#
# class Producto(models.Model):
#     nombre = models.CharField(max_length=200, unique=True)
#     tipo = models.CharField(max_length=100)
#     stock = models.IntegerField(default=0)
#     stock_minimo = models.IntegerField(default=0)
#     fecha_caducidad = models.DateField(null=True, blank=True)
#
#     def __str__(self):
#         return self.nombre
#
#     def stock_bajo(self):
#         return self.stock < self.stock_minimo
#
#     from gestion.models import CustomUser
#
#     def crear_usuario_admin(self):
#         user = CustomUser.objects.create_user(
#             username='admin_user',
#             password='secure_password',
#             email='admin@example.com',
#             role='admin',
#         )
#         user.is_superuser = True
#         user.is_staff = True
#         user.save()
#
#
#
#
#
#
