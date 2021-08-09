import csv

file = open("Books.csv","r")
for row in file:
    print(row)
file.close()

qst = input("¿Desea ingresar otro campo? (s/n)\n")
qst = qst.lower()

if qst == "s":
    file = open("Books.csv","a")
    nameb = input("Ingrese el nombre del libro: ")
    nameb = nameb.lower()
    nameb = nameb.capitalize()
    author = input("Ingrese el autor de la obra: ")
    author = author.lower()
    author = author.capitalize()
    year = input("Ingrese el año de publicación: ")
    newRecord = nameb+","+author+","+year+"\n"
    file.write(str(newRecord))
    file.close()

file = open("Books.csv","r")
for row in file:
    print(row)
file.close()