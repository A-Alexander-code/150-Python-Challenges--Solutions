list = [157,746,359,789]

for i in list:
    print(i)

qst = int(input("Ingrese un número de tres digitos\n"))

if qst in list:
    print(qst,"existe dentro de la lista en la posición",list.index(qst))
else:
    print("No existe dentro de la lista")