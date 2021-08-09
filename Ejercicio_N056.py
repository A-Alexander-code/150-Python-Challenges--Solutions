#Mi solución difiere del libro
import random
num1 = random.randint(1,10)
num2 = int(input("Ingrese un número: "))
while num2 != num1:
    print("El número no es el correcto")
    num2 = int(input("Ingrese un número: "))

print("Has acertado")