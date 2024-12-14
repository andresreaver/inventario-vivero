from gestion.models.cliente import Cliente, Responsabilidad

def listar_responsabilidades():
    return Responsabilidad.objects.all()

def crear_responsabilidades():
    # Crear responsabilidades si no existen (solo al inicializar el sistema)
    responsabilidades = [
        ("01", "Aporte especial para la administración de justicia"),
        ("02", "Gravamen a los Movimientos Financieros (GMF)"),
        # Agregar las demás responsabilidades aquí...
    ]
    for codigo, descripcion in responsabilidades:
        Responsabilidad.objects.get_or_create(codigo=codigo, descripcion=descripcion)

def crear_cliente(datos):
    cliente = Cliente.objects.create(**datos)
    return cliente

def actualizar_cliente(cliente_id, datos):
    cliente = Cliente.objects.get(id=cliente_id)
    for key, value in datos.items():
        setattr(cliente, key, value)
    cliente.save()
    return cliente
