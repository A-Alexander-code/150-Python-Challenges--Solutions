file = open("Names.txt","a")
qst = input("¿Desea agregar un nombre? (s/n)\n")
qst = qst.lower()

if qst == "s":
    name = input("Ingrese el nombre: ")
    name = name.lower()
    name = name.capitalize()
    file.write(name + "\n")
    file.close()

file = open("Names.txt","r")
print(file.read())
file.close()