# Escribe un programa que solicite al usuario un índice para acceder a un elemento de una lista
# predefinida. Maneja posibles errores si el índice ingresado está fuera del rango de la lista o
# si el usuario ingresa un valor no numérico.

elementos = ["manzana", "banana", "cereza", "durazno", "kiwi"]

try:
    entrada = input(
        "Ingresa el índice de un elemento (0 a {}): ".format(len(elementos) - 1)
    )

    indice = int(entrada)

    print("Elemento en el índice", indice, "es:", elementos[indice])

except ValueError:
    print("Error: Debes ingresar un número entero.")

except IndexError:
    print(
        "Error: El índice está fuera del rango. Debe ser entre 0 y", len(elementos) - 1
    )
