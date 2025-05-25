# Escribe un programa para mostrar los números
# pares[1]
# desde 0 hasta 20.

numero = 0

while numero < 20:
    numero += 1
    if (numero % 2) != 0:
        continue
    print(numero)
