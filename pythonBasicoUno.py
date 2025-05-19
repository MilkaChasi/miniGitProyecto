# Verificación de edad
# Implementa un programa que solicite la edad y que este determine
# si la persona es menor de edad, mayor o tiene edad de jubilación.
nombre = input("Ingrese su nombre: ")
edad= int(input("Ingrese tu edad: "))

if (edad < 18):
    print(f"¡Hola {nombre}! Eres menor de edad aún.")
elif (edad >= 60):
    print(f"¡Hola {nombre}! Usted ya tiene la edad para jubilarse.")
else:
    print(f"¡Hola {nombre}! Eres mayor de edad.")
