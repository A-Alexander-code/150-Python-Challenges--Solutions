list = [[2,5,8],[3,7,4],[1,6,9],[4,2,0]]

row = int(input("Elija una fila para mostrar: "))
print(list[row])

val = int(input("Ingrese un valor para agregarse: "))

list[row].append(val)

print(list[row])