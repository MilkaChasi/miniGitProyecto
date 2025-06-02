# Convierte la lista ['a', 'b', 'c'] en tupla, e intenta agregar un elemento nuevo (observa qué sucede).

lista = ["a", "b", "c"]

# Como es una tupla no se puede modificar
# print(tuple(lista).append("s"))

lista.append("z")
print(tuple(lista))
