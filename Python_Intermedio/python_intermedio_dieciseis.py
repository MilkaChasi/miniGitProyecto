# Define la función presentarse(nombre, edad=None)
# que imprima un mensaje distinto según si se conoce la edad o no.


def presentarse(nombre, edad=None):
    """
    Devuelve los datos completos si existe un valor asignado a cada parámetro.

    Parámetros:
    nombre (str): Nombre de la persona.
    edad (int): Edad de la persona.

    """
    if edad is not None:
        print(f"Sus datos son: nombre es {nombre} y su edad es {edad} ")
    else:
        print(f"Su información es: nombre es {nombre}")


presentarse("Milka", 25)
presentarse("Monica")
