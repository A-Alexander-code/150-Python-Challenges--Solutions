comida = {}
key1 = input("¿Cuál es su platillo favorito?\n")
comida[1] = key1 
key2 = input("¿Cuál es su platillo favorito?\n")
comida[2] = key2 
key3 = input("¿Cuál es su platillo favorito?\n")
comida[3] = key3
key4 = input("¿Cuál es su platillo favorito?\n")
comida[4] = key4 
print(comida)
qst = int(input("Ingrese el indice del platillo que desea eliminar: "))
del comida[qst]
print(comida)