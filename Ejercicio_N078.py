tvprom = ["Lost","Breaking Bad","The Flash","Mr. Robot"]
for i in tvprom:
    print(i)
    
qst = input("¿Desea ingresar un nuevo programa de televisión? (s/n)\n")

if qst == "s":
    name = input("Ingrese el nombre del programa\n")
    pos = int(input("Ingrese la posición dentro de la lisata\n"))
    pos = pos - 1
    tvprom.insert(pos,name)
else:
    print("La lista se guardara sin cambios")

for i in tvprom:
    print(i)