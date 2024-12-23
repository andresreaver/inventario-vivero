# Generated by Django 5.1.3 on 2024-12-16 03:39

import django.contrib.auth.models
import django.contrib.auth.validators
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
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
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200, unique=True)),
                ('tipo', models.CharField(max_length=100)),
                ('stock', models.IntegerField(default=0)),
                ('stock_minimo', models.IntegerField(default=0)),
                ('fecha_caducidad', models.DateField(blank=True, null=True)),
                ('precio_compra', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('precio_venta', models.DecimalField(decimal_places=2, max_digits=10)),
                ('activo', models.BooleanField(default=True)),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('modificado', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_razon_social', models.CharField(max_length=255)),
                ('nit_cedula', models.CharField(max_length=50, unique=True)),
                ('tipo_documento', models.CharField(choices=[('31', 'NIT'), ('13', 'Cédula'), ('22', 'Cédula de Extranjería'), ('43', 'Código Extranjero'), ('12', 'Tarjeta de Identidad'), ('11', 'Registro Civil'), ('41', 'Pasaporte')], max_length=2)),
                ('telefono', models.CharField(max_length=15)),
                ('correo_electronico', models.EmailField(max_length=254)),
                ('direccion', models.TextField()),
                ('tipo_cuenta', models.CharField(blank=True, choices=[('Ahorros', 'Ahorros'), ('Corriente', 'Corriente')], max_length=10, null=True)),
                ('numero_cuenta', models.CharField(blank=True, max_length=20, null=True)),
                ('entidad_bancaria', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Responsabilidad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=3, unique=True)),
                ('descripcion', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ResponsabilidadProveedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=3, unique=True)),
                ('descripcion', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('role', models.CharField(choices=[('admin', 'Administrador'), ('user', 'Usuario')], default='user', max_length=10)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('numero_factura', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateTimeField(default=django.utils.timezone.now)),
                ('forma_pago', models.CharField(choices=[('Efectivo', 'Efectivo'), ('Tarjeta de Credito', 'Tarjeta de Credito'), ('Tarjeta Debito', 'Tarjeta Debito')], max_length=100)),
                ('subtotal', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('iva', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='facturas', to='gestion.cliente')),
            ],
        ),
        migrations.CreateModel(
            name='MovimientoInventario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_movimiento', models.CharField(choices=[('compra', 'Compra'), ('venta', 'Venta')], max_length=10)),
                ('cantidad', models.PositiveIntegerField()),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('tipo_pago', models.CharField(blank=True, max_length=50, null=True)),
                ('precio_total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('cliente', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion.producto')),
            ],
        ),
        migrations.CreateModel(
            name='Detalle_factura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveIntegerField()),
                ('precio_unitario', models.DecimalField(decimal_places=2, max_digits=10)),
                ('subtotal', models.DecimalField(decimal_places=2, max_digits=10)),
                ('factura', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='detalles', to='gestion.factura')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion.producto')),
            ],
        ),
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveIntegerField()),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('precio_unitario', models.DecimalField(decimal_places=2, max_digits=10)),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='compras', to='gestion.producto')),
                ('proveedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='compras', to='gestion.proveedor')),
            ],
        ),
        migrations.AddField(
            model_name='proveedor',
            name='responsabilidades',
            field=models.ManyToManyField(blank=True, related_name='proveedores', to='gestion.responsabilidad'),
        ),
        migrations.AddField(
            model_name='cliente',
            name='responsabilidades',
            field=models.ManyToManyField(blank=True, related_name='clientes', to='gestion.responsabilidad'),
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveIntegerField()),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('precio_unitario', models.DecimalField(decimal_places=2, max_digits=10)),
                ('precio_total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ventas', to='gestion.cliente')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion.producto')),
            ],
        ),
    ]
