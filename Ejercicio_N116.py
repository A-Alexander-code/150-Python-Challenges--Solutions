import csv

file = list(csv.reader(open("Books.csv")))
Booklist = []
for row in file:
    Booklist.append(row)

f = 0
for row in Booklist:
    display = f, Booklist[f]
    print(display)
    f += 1
    
getrid = int(input("Ingrese el número de fila a eliminar: "))
del Booklist[getrid]

f = 0
for row in Booklist:
    display = f, Booklist[f]
    print(display)
    f += 1
    
alter = int(input("¿Qué fila desea editar?\n"))
f = 0
for colm in Booklist[alter]:
  display = f,Booklist[alter][f]
  print(display)
  f += 1
part = int(input("¿Qué sección desea cambiar?\n"))
newData = input("Ingrese el nuevo valor: ")
Booklist[alter][part] = newData
print(Booklist[alter])

file = open("Books.csv","w")
f = 0
for row in Booklist:
    newrecord = Booklist[f][0] +","+Booklist[f][1]+","+Booklist[f][2]+"\n"
    file.write(newrecord)
    f += 1
file.close()

