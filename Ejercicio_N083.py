letra = input("Ingrese un mensaje en mayúscula: ")
correct = letra.upper()
while letra != correct:
    print("Error. No es el formato indicado, intentelo denuevo")
    letra = input("Ingrese una letra en mayúscula: ")
    correct = letra.upper()

print("Gracias")