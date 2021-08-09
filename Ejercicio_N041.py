num = int(input("Ingrese un número: "))
if num <= 10:
    name = input("Ingrese su nombre: ")
    for i in range(0,num+1):
        print(name)
else:
    for j in range(0,3):
        print("Demasiado alto")
        