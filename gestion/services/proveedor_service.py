from gestion.models.proveedor import Proveedor, Responsabilidad

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

def crear_proveedor(datos):
    proveedor = Proveedor.objects.create(**datos)
    return proveedor

def actualizar_proveedor(proveedor_id, datos):
    proveedor = Proveedor.objects.get(id=proveedor_id)
    for key, value in datos.items():
        setattr(proveedor, key, value)
    proveedor.save()
    return proveedor
