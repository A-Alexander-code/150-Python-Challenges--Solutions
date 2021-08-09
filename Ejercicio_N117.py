import csv
import random

score = 0
name = input("Ingrese su nombre: ")
num1 = random.randint(10,50)
num2 = random.randint(10,50)
resp1 = (num1 + num2)*num1
resp2 = (num1**2)/num1
qst1 = "("+str(num1)+" + "+str(num2)+")"+" * "+str(num1)
print(qst1)
answ1 = int(input("Ingrese la respuesta del primer ejercicio: "))
if answ1 == resp1:
    score += 1
qst2 = "("+str(num1)+"^2)"+" / "+str(num2)
print(qst2)
answ2 = float(input("Ingrese la respuesta del segundo ejercicio: "))
if answ2 == resp2:
    score += 1

file = open("Quiz.csv","w")
newrecord = name+","+qst1+","+str(resp1)+","+qst2+","+str(resp2)+","+str(score)+"\n"
file.write(newrecord)
file.close()
