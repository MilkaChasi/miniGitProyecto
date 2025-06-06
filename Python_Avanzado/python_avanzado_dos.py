# Escribe un programa que recorra una lista con diferentes tipos de datos e
# intente sumar solo los valores numéricos.
# Usa try/except para manejar errores si los elementos no son números.

frutas = ["manzana", "banana", "cereza", "durazno", "kiwi"]
numeros = [1, 2, 3]
sets = {"animal": "perro"}
datos = [frutas, numeros, sets]

suma_total = 0

for grupo in datos:
    try:
        if isinstance(grupo, (dict, str)):
            raise TypeError

        for elemento in grupo:
            if isinstance(elemento, (int, float)):
                suma_total += elemento
    except TypeError:
        print(f"No se puede iterar sobre: {grupo})")

print("Suma total de los valores numéricos:", suma_total)
