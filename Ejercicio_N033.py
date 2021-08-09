import math
print("Ingrese dos números enteros. Siendo el primero mayor que el segundo")
num1 = int(input("Ingrese el primer número\n"))
num2 = int(input("Ingrese el segundo número\n"))
res1 = num1 // num2
res2 = num1 % num2
print("Si se ingresa",num1,"y se divide para",num2,"se obtiene",res1,"con",res2,"de remanente")