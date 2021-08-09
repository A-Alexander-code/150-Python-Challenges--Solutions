pass01 = input("Ingrese una contraseña de 4 carácteres\n")
pass02 = input("Vuelva a ingresar la contraseña\n")

if pass01 == pass02:
    print("La contraseña es correcta y se guardara")
elif pass01.lower() == pass02.lower():
    print("Los carácteres de ambas contraseñas deben ser iguales")
else:
    print("¡Incorrecto!")