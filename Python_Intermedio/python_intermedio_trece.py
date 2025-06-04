# Define la función es_par(n) que devuelva True si n es par y False si es impar.


def es_par(n):
    """
    Devuelve True si n es un número par, False si es impar.

    Parámetros:
    n (int): Número entero a evaluar.

    Retorna:
    bool: True si n es par, False en caso contrario.
    """
    if n % 2 == 0:
        return True
    else:
        return False


print(es_par(5))

print(es_par(8))
