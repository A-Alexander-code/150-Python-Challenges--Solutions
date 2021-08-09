num = int(input("Ingresa un número entre el 10 y el 20\n"))
while num < 10 or num > 20:
    if num < 10:
        print("Demasiado bajo")
    else:
        print("Demasiado alto")
    num = int(input("Ingresa un número entre el 10 y el 20\n"))

print("Gracias")