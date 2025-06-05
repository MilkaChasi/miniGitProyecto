# Dada la lista nums = [1,2,3] y el diccionario datos = {'a': 10, 'b': 20},
# llama a una función que acepte *args y **kwargs usando *nums y **datos.


def aceptar_datos(*nums, **datos):
    """
    Imprime números posicionales y datos con clave recibidos como *args y **kwargs.

    Parámetros:
    *nums (tuple): Números recibidos como argumentos posicionales.
    **datos (dict): Pares clave-valor recibidos como argumentos con nombre.
    """
    for numeros in nums:
        print(numeros)

    for clave, valor in datos.items():
        print(f"{clave:<2}: {valor}")

    return nums, datos


nums = [1, 2, 3]
datos = {"a": 10, "b": 20}

print(f"en una sola linea: {aceptar_datos(*nums, **datos)}")
