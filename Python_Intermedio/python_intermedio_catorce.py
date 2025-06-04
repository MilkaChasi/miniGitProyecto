# Llama a una función saludar_persona() usando parámetros en distinto orden con nombre (keyword).


def saludar_persona(nombre, apellido):
    """
    Devuelve el nombre de la persona y su apellido.

    Parámetros:
    nombre (str): Nombre de la persona.
    apellido (str): Apellido de la persona.

    Retorna:
    str: Una cadena con nombre completo.
    """
    return nombre + " " + apellido


print(f'Hola {saludar_persona(apellido = "Pozo", nombre = "Fernando")}')
