import csv

#Conocer el número de filas del archivo .csv
file = open("Books.csv")
reader = csv.reader(file)
lines = len(list(reader))

styear = int(input("Ingrese un año de inicio: "))
ndyear = int(input("Ingrese un año de conclusión: "))


file = list(csv.reader(open("Books.csv")))
tmp = []
for row in file:
    tmp.append(row)

f = 0

for row in tmp:
    if styear <= int(tmp[f][2]) <= ndyear:
        print(tmp[f])  
    f = f + 1

