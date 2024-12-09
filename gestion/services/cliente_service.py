from gestion.models.cliente import Cliente

class ClienteService:
    @staticmethod
    def crear_cliente(nombre, telefono, email, direccion):
        cliente = Cliente(nombre=nombre, telefono=telefono, email=email, direccion=direccion)
        cliente.save()
        return cliente

    @staticmethod
    def obtener_clientes():
        return Cliente.objects.all()
