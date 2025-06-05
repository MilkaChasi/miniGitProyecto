# Crea una función listar_alumnos(*nombres)
# que imprima cada nombre recibido en una nueva línea.


def listar_alumnos(*nombres):
    """
    Imprime cada nombre recibido en una nueva línea.

    Parámetros:
    *nombres (str): Una cantidad variable de nombres de alumnos.
    """
    for nombre in nombres:
        print(nombre)


listar_alumnos("Karla", "Jose", "Pedro", "Luis")
