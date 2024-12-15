from gestion.models.cliente import Cliente, Responsabilidad

class ClienteService:
    @staticmethod
    def listar_responsabilidades():
        return Responsabilidad.objects.all()

    @staticmethod
    def crear_responsabilidades():
        responsabilidades = [
            ("01", "Aporte especial para la administración de justicia"),
            ("02", "Gravamen a los Movimientos Financieros (GMF)"),
            # Agregar las demás responsabilidades aquí...
        ]
        for codigo, descripcion in responsabilidades:
            Responsabilidad.objects.get_or_create(codigo=codigo, descripcion=descripcion)

    @staticmethod
    def crear_cliente(datos):
        cliente = Cliente.objects.create(**datos)
        return cliente

    @staticmethod
    def actualizar_cliente(cliente_id, datos):
        cliente = Cliente.objects.get(id=cliente_id)
        for key, value in datos.items():
            setattr(cliente, key, value)
        cliente.save()
        return cliente
