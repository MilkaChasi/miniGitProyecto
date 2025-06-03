# Elimina un elemento con pop() y luego verifica si la clave aún existe usando in.

alumnos = {"Pedro": "Zambrano", "Kamila": "Lopez", "Lorena": "Moran", "Norma": "Perez"}
alumnos.pop("Kamila")

for alumno in alumnos.keys():
    print(alumno)

for alumno in alumnos.values():
    print(alumno)

for nombre, apellido in alumnos.items():
    print(nombre, " = ", apellido)
