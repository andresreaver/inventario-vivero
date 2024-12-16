# Modelo  para cliente
from django.db import models


<<<<<<< HEAD
=======

>>>>>>> origin/AndresReaver02
class Cliente(models.Model):
    TIPOS_DOCUMENTO = [
        ('31', 'NIT'),
        ('13', 'Cédula'),
        ('22', 'Cédula de Extranjería'),
        ('43', 'Código Extranjero'),
        ('12', 'Tarjeta de Identidad'),
        ('11', 'Registro Civil'),
        ('41', 'Pasaporte'),
    ]

    nombre_razon_social = models.CharField(max_length=255)
    nit_cedula = models.CharField(max_length=50, unique=True)
    tipo_documento = models.CharField(max_length=2, choices=TIPOS_DOCUMENTO)
    telefono = models.CharField(max_length=15)
    correo_electronico = models.EmailField()
    direccion = models.TextField()

    responsabilidades = models.ManyToManyField(
        'Responsabilidad',
        related_name='clientes',
        blank=True
    )

    def __str__(self):
        return self.nombre_razon_social


<<<<<<< HEAD
class Responsabilidad_cliente(models.Model):
=======
class Responsabilidad(models.Model):  # Cambiar el nombre del modelo
>>>>>>> origin/AndresReaver02
    codigo = models.CharField(max_length=3, unique=True)
    descripcion = models.TextField()

    def __str__(self):
<<<<<<< HEAD
        return f"{self.codigo}. {self.descripcion}"
=======
        return f"{self.codigo}. {self.descripcion}"
>>>>>>> origin/AndresReaver02
