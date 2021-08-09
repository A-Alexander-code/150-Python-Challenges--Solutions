list = {}

for i in range (0,4):

    name = input("Ingrese un nombre: ")
    name = name.lower()
    name = name.capitalize()
    age = int(input("Ingrese la edad: "))
    zsize = int(input("Ingrese la talla de calzado: "))
    
    list[name] = {"Age":age,"Shoe size":zsize}

for j in list:
    print(j)

nombre = input("Ingrese el nombre que desea retirar de la lista: ")
nombre = nombre.lower()
nombre = nombre.capitalize()

del list[nombre]

for name in list:
    print((name), list [name]["Age"], list[name]["Shoe size"])