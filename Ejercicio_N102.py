list = {}

for i in range (0,4):

    name = input("Ingrese un nombre: ")
    name = name.lower()
    name = name.capitalize()
    age = int(input("Ingrese la edad: "))
    zsize = int(input("Ingrese la talla de calzado: "))
    
    list[name] = {"Age":age,"Shoe size":zsize}

for name in list:
    print(name)

ask = input("Ingrese un nombre a consultar: ")
ask = ask.lower()
ask = ask.capitalize()

print(list[ask])
    

