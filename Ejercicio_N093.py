from array import *

nums = array("i",[])

for i in range(0,5):
    num = int(input("Ingrese un número: "))
    nums.append(num)

nums = sorted(nums)

for i in nums:
    print(i)
    
qst = int(input("¿Ingrese el número que desea eleminar de la lista?\n"))

if qst in nums:
    nums.remove(qst)
    nums2 = array("i",[])
    nums2.append(qst)
    nums2 = sorted(nums2)
    print(nums)
    print(nums2)
else:
    print("El número no se encuentra dentro de la matriz")
