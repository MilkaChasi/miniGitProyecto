# Crea un programa que solicite al usuario ingresar una contraseña y
# valide si cumple con los siguientes criterios:
# Debe tener al menos 8 caracteres.
# Debe contener al menos un número.
# Debe incluir al menos una letra mayúscula.

# Si la contraseña no cumple con alguno de estos requisitos,
# el programa mostrará el mensaje de error correspondiente y
# volverá a pedir la contraseña hasta que el usuario ingrese una válida.


def validar_contrasena(contrasena):
    """Validación de contraseña con parámetros"""
    errores = []

    if len(contrasena) < 8:
        errores.append("La contraseña debe tener al menos 8 caracteres.")
    if not any(c.isdigit() for c in contrasena):
        errores.append("La contraseña debe contener al menos un número.")
    if not any(c.isupper() for c in contrasena):
        errores.append("La contraseña debe incluir al menos una letra mayúscula.")

    return errores


while True:
    try:
        contrasena = input("Ingresa una contraseña: ")
        if contrasena is None:
            raise ValueError("Entrada inválida")

        errores = validar_contrasena(contrasena)

        if not errores:
            print("¡Contraseña válida!")
            break
        else:
            for error in errores:
                print("Error:", error)
            print("Inténtalo nuevamente.\n")

    except Exception as e:
        print("Ocurrió un error inesperado:", e)
