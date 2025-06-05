# Crea una función crear_cita(**info) que reciba datos como
# fecha, hora, descripcion y los imprima en un formato de cita


def crear_cita(**info):
    """
    Imprime los datos de una cita en un formato legible.

    Parámetros:
    **info (dict): Datos como fecha, hora, descripción, etc.
    """
    for clave, valor in info.items():
        print(f"{clave.capitalize():<12}: {valor}")


crear_cita(fecha="25/06/1998", hora="10:05:00", descripcion="Medicina General")
