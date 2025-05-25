# Implementa un programa que muestre opciones de un menú (3 como máximo) y
# permita elegir una de estas opciones (deberá mostrar la opción que escogí).
# En el caso de que se ingrese una opción que no esté dentro de las 3 opciones establecidas,
# deberá mostrarme un mensaje de error (algo así como opción inválida).

pedido = input("¿Qué va a ordenar? ")

menu_uno = ["agua", "sanduche", "manzana"]
menu_dos = ["soda", "arroz", "pollo"]
menu_tres = ["sopa", "jugo"]

if pedido in menu_uno:
    print(f"Has ordenado '{pedido}' del Menú 1.")
elif pedido in menu_dos:
    print(f"Has ordenado '{pedido}' del Menú 2.")
elif pedido in menu_tres:
    print(f"Has ordenado '{pedido}' del Menú 3.")
else:
    print("Opción inválida. Ese producto no está en el menú.")
