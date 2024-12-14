from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=200)
    cedula = models.CharField(max_length=20, unique=True)  # Identificación única
    direccion = models.CharField(max_length=300, blank=True, null=True)
    telefono = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} ({self.cedula})"
