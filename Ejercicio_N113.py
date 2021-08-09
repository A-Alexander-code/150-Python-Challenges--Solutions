import csv

file = open("Books.csv","r")
for row in file:
    print(row)
file.close()

qst = int(input("¿Cuántos campos desea agregar?\n"))

file = open("Books.csv","a")
for i in range(0,qst):
    nameb = input("Ingrese el nombre del libro: ")
    author = input("Ingrese el autor de la obra: ")
    year = input("Ingrese el año de publicación: ")
    print("--------------------------------")
    newRecord = nameb+","+author+","+year+"\n"
    file.write(str(newRecord))
file.close()

file = open("Books.csv","r")
for row in file:
    print(row)
file.close()

search = input("Ingrese un autor del que quiera obtener información \n")

file = open("Books.csv","r")
cont = 0

for row in file:
    if search in str(row):
        print(row)
        cont = cont + 1
if cont == 0:
    print("No hay campos que coincidan con la busqueda")
    
file.close()