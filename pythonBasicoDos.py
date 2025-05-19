# Contraseña correcta
# Implementa un programa que solicite una contraseña y verifica si es correcta o incorrecta.
# “Tú defines cuál es la contraseña correcta”.

contraseña_recibida = input("Ingresa una contraseña que tu creas que es la correcta: ")
contraseña_esperada = "contra1235"

if(contraseña_recibida == contraseña_esperada):
    print("La contraseña ingresada es la correcta. ¡FELICITACIONES!")
else:
    print("La contraseña imgresa es incorrecta. Vuelve a intentar")