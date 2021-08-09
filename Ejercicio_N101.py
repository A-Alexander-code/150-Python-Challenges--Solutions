sales = {"John":{"N":3056,"S":8463,"E":8441,"W":2694},
         "Tom":{"N":4832,"S":6786,"E":4737,"W":3612},
         "Anne":{"N":5239,"S":4802,"E":5820,"W":1859},
         "Fiona":{"N":3904,"S":3645,"E":8821,"W":2451}
         }
print("John ",sales["John"])
print("Tom  ",sales["Tom"])
print("Anne ",sales["Anne"])
print("Fiona",sales["Fiona"])

qstn1 = input("Ingrese un nombre: ")
qstn1 = qstn1.lower()
qstn1 = qstn1.capitalize()

qstr1 = input("Ingrese una región: ")
qstr1 = qstr1.lower()
qstr1 = qstr1.capitalize()

print(sales[qstn1][qstr1])

val = int(input("Ingrese el nuevo valor asociado a la celda que eligió: "))

sales[qstn1][qstr1] = val

print(qstn1," ",sales[qstn1])