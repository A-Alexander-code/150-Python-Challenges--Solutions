name = input("Ingrese su nombre: ")
name = name.lower()
cont = 0
for i in name:
    if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
        cont = cont + 1
    else:
        cont = cont
        
print("Su nombre tiene",cont,"vocales")

