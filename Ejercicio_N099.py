list = [[2,5,8],[3,7,4],[1,6,9],[4,2,0]]
print(list)

row = int(input("Elija una fila para mostrar: "))
column = int(input("Elija una columna para mostrar: "))
print(list[row][column])

qst = input("¿Desea cambiar el valor de la celda? (s/n)\n")

if qst == "s":
    val = int(input("Ingrese el nuevo valor: "))
    list[row][column] = val
    print(list[row])
else:
    print("No se ha realizado ningún cambio")




