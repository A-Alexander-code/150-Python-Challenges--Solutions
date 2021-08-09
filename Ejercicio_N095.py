from array import *
import random

nums = array("f",[])

for i in range (0,5):
    num1 = random.randint(20,1000)
    num2 = random.randint(5,50)
    num3 = num1/num2
    nums.append(num3)
    

for i in nums:
    print(round(i,2))
    
atry = True

while atry == True:
    qst = int(input("Ingrese un número entero entre el 2 y el 5: "))
    if 2 <= qst <= 5:
        nums2 = array("f",[])
        for i in nums:
            x = i/qst
            nums2.append(x)
        for i in nums2:
            print(round(i,2))
        atry = False
    else:
        print("El número no se encuentra en rango")