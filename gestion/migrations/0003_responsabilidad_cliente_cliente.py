# Generated by Django 5.1.3 on 2024-12-14 01:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0002_responsabilidad_alter_proveedor_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Responsabilidad_cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=3, unique=True)),
                ('descripcion', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_razon_social', models.CharField(max_length=255)),
                ('nit_cedula', models.CharField(max_length=50, unique=True)),
                ('tipo_documento', models.CharField(choices=[('31', 'NIT'), ('13', 'Cédula'), ('22', 'Cédula de Extranjería'), ('43', 'Código Extranjero'), ('12', 'Tarjeta de Identidad'), ('11', 'Registro Civil'), ('41', 'Pasaporte')], max_length=2)),
                ('telefono', models.CharField(max_length=15)),
                ('correo_electronico', models.EmailField(max_length=254)),
                ('direccion', models.TextField()),
                ('responsabilidades', models.ManyToManyField(blank=True, related_name='clientes', to='gestion.responsabilidad')),
            ],
        ),
    ]