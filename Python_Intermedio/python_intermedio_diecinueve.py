# Crea una función crear_multiplicador(n)
# que retorne otra función que multiplica su argumento por n.
# Usa esa función para crear un duplicador y un triplicador.


def crear_multiplicador(n):
    """
    Crea una función que multiplica su argumento por n.

    Parámetros:
    n (int): El número por el cual se multiplicará.

    Retorna:
    function: Una función que toma un argumento y lo multiplica por n.
    """

    def multiplicador(x):
        return x * n

    return multiplicador


duplicador = crear_multiplicador(2)
triplicador = crear_multiplicador(3)

print(duplicador(5))
print(triplicador(5))
