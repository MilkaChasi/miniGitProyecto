# Define una función que devuelva en una tupla la suma y
# la diferencia de dos números y captura ambos valores en variables.


def operaciones(a, b):
    """
    Devuelve en tuplas la suma y diferencia de dos cantidades.

    Parámetros:
    a (int): Número entero a evaluar.
    b (int): Número entero a evaluar.

    Retorna:
    Suma (int): suma de dos cantidades.
    Diferencia (int): resta de dos cantidades.
    """
    return (a + b, a - b)


Suma, Diferencia = operaciones(9, 8)
print(f"Suma:{Suma} y Diferencia:{Diferencia}")
