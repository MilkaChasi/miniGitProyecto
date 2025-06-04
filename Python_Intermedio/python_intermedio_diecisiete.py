# Define una función sencilla (por ejemplo, que sume 2) y
# úsala con map() para aplicarla sobre una lista de números.


def suma(a):
    """Definicion de una suma de valores"""
    return a + 2


lista = [1, 2, 3, 4, 5]
lista_suma = list(map(suma, lista))

print(lista_suma)
