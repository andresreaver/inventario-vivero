from gestion.materiaprima.materia_prima import MateriaPrima

class MateriaPrimaService:
    @staticmethod
    def crear_materia_prima(nombre, stock, stock_minimo, proveedor):
        materia_prima = MateriaPrima(nombre=nombre, stock=stock, stock_minimo=stock_minimo, proveedor=proveedor)
        materia_prima.save()
        return materia_prima

    @staticmethod
    def obtener_materias_primas():
        return MateriaPrima.objects.select_related('proveedor').all()
