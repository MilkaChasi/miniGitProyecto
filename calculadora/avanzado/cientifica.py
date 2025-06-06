"""Módulo científica: contiene la funcion para obtener la raíz cuadrada usando el módulo math."""

import math


def raiz_cuadrada(x):
    """Devuelve la raíz cuadrada de x."""
    if x < 0:
        return "Error: no se puede calcular la raíz cuadrada de un número negativo"
    return math.sqrt(x)
