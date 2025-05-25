# Verificación de número mayor
# Implementa un programa que solicite dos números, determina cuál es el mayor, o si son iguales.

numero_primero = int(input("Ingresa un valor numérico: "))
numero_dos = int(input("Ingresa un valor numérico: "))

if numero_primero > numero_dos:
    print(f"El primer valor ingresado {numero_primero} es mayor al segundo valor {numero_dos}")
elif numero_primero == numero_dos:
    print(f"El primer valor ingresado {numero_primero} es igual al segundo valor {numero_dos}")
else:
    print(f"El primer valor ingresado {numero_primero} es menor al segundo valor {numero_dos}")