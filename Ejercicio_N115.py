import csv

file = open("Books.csv","r")
for row in file:
    print(row)
file.close()

file = open("Books.csv","r")
f = 0
for row in file:
    display = "Row: "+str(f)+"-"+row
    print(display)
    f += 1