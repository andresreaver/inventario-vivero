from gestion.proveedor.proveedor import Proveedor

class ProveedorService:
    @staticmethod
    def crear_proveedor(nombre, telefono, email, direccion):
        proveedor = Proveedor(nombre=nombre, telefono=telefono, email=email, direccion=direccion)
        proveedor.save()
        return proveedor

    @staticmethod
    def obtener_proveedores():
        return Proveedor.objects.all()

    @staticmethod
    def actualizar_proveedor(proveedor_id, nombre, telefono, email, direccion):
        proveedor = Proveedor.objects.get(id=proveedor_id)
        proveedor.nombre = nombre
        proveedor.telefono = telefono
        proveedor.email = email
        proveedor.direccion = direccion
        proveedor.save()
        return proveedor

    @staticmethod
    def eliminar_proveedor(proveedor_id):
        proveedor = Proveedor.objects.get(id=proveedor_id)
        proveedor.delete()
