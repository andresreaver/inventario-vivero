# Modelo  para Proveedor
from django.db import models

class Proveedor(models.Model):
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
        related_name='proveedores',
        blank=True
    )

    tipo_cuenta = models.CharField(
        max_length=10,
        choices=[('Ahorros', 'Ahorros'), ('Corriente', 'Corriente')],
        null=True,
        blank=True
    )
    numero_cuenta = models.CharField(max_length=20, null=True, blank=True)
    entidad_bancaria = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.nombre_razon_social


# En gestion/models/proveedor.py
class ResponsabilidadProveedor(models.Model):  # Cambiar el nombre aquí
    codigo = models.CharField(max_length=3, unique=True)
    descripcion = models.TextField()

    def __str__(self):
        return f"{self.codigo}. {self.descripcion}"
