from array import *

nums = array("i",[])

for i in range(0,5):
    num = int(input("Ingrese un número entre el 10 y 20\n"))
    if 10<= num <= 20:
        nums.append(num)
    else:
        print("Fuera de rango")

print("Gracias")
for i in nums:
    print(i)