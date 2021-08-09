#Mi solución difiere del libro
import random
num1 = random.randint(1,10)
num2 = int(input("Ingrese un número: "))
while num2 != num1:
    if num2 < num1:
        print("El número es menor al original")
        num2 = int(input("Ingrese un número: "))
    else:
        print("El número es mayor al original")
        num2 = int(input("Ingrese un número: "))

print("Has acertado")