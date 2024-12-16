from gestion.models.cliente import Cliente

class ClienteService:
    @staticmethod
    def crear_cliente(nombre, cedula, direccion=None, telefono=None):
        """Crea un cliente nuevo."""
        return Cliente.objects.create(
            nombre=nombre,
            cedula=cedula,
            direccion=direccion,
            telefono=telefono
        )

    @staticmethod
    def obtener_cliente_por_id(cliente_id):
        """Obtiene un cliente por su ID."""
        return Cliente.objects.get(id=cliente_id)

    @staticmethod
    def obtener_clientes():
        """Devuelve una lista de todos los clientes."""
        return Cliente.objects.all()

    @staticmethod
    def actualizar_cliente(cliente_id, **datos):
        """Actualiza un cliente existente."""
        cliente = Cliente.objects.get(id=cliente_id)
        for key, value in datos.items():
            setattr(cliente, key, value)
        cliente.save()
        return cliente
