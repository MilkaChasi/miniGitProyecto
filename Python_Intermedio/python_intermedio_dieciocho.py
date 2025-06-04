# Crea una lista que contenga dos o tres funcioness
# (por ejemplo str.lower, str.upper)
# y aplica cada una a la misma cadena.


def minuscula(a):
    """Transformar a minúsculas."""
    return a.lower()


def mayusculas(a):
    """Transformar a mayúsculas."""
    return a.upper()


def reemplazo(a):
    """Reemplaza todas las apariciones de a por b."""
    return a.replace("a", "A")


funciones = [minuscula, mayusculas, reemplazo]
texto = "La casA es amArilla"

resultados = [funcion(texto) for funcion in funciones]
print(resultados)
