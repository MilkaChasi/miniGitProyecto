# Escribe un programa para mostrar los números
# pares[1]
# desde 0 hasta 20.

for numero in range(0, 21):
    numero += 1
    if (numero % 2) != 0:
        continue
    print(numero)
