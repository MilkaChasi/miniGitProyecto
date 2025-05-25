# Crea un programa que pida una contraseña hasta que sea correcta.
# “Tú defines cuál es la contraseña correcta”.

contraseña_esperada = "1234password"
contraseña = ""

while contraseña != contraseña_esperada:
    contraseña =  input("Ingresar contraseña: ")
    if contraseña == contraseña_esperada:
        print("contraseña correcta!!")
    else:
        print("contraseña incorrecta! Vuelva a intentar")
