from django.core.exceptions import ValidationError

def validar_stock_positivo(value):
    if value < 0:
        raise ValidationError("El stock debe ser un valor positivo.")
