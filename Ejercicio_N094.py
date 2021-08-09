from array import *

nums = array("i",[125,326,167,138,118])
for i in nums:
    print(i)

num = int(input("Ingrese un número de la matriz: "))
retry = True 

while retry == True:
    if num in nums:
        id = nums.index(num)
        print("El número",num,"se encuentra en la posición",id)
        retry = False
    else:
        print("El número no está dentro del campo. Intente de nuevo")
        num = int(input("Ingrese un número de la matriz: "))