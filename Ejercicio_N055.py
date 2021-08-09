import random
num1 = random.randint(1,5)
num2 = int(input("Ingrese un número: "))
if num2 == num1:
    print("¡Buen trabajo!")
elif num2 > num1:
    print("Muy alto")
    num2 = int(input("Ingrese otro número: "))
    if num2 == num1:
        print("¡Buen trabajo!")
    else:
        print("Has perdido :(")
elif num2 < num1:
    print("Muy bajo")
    num2 = int(input("Ingrese otro número: "))
    if num2 == num1:
        print("¡Buen trabajo!")
    else:
        print("Has perdido :(")       