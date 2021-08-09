num = int(input("¿Cuántas personas invitara a la fiesta?\n"))
if num < 10:
    for i in range(0,num):
        inv = input("Ingrese el nombre del invitado: ")
        print(inv,"ha sido agregado a la lista")
else:
    print("Demasiadas personas")