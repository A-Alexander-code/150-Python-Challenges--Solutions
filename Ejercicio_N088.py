from array import *

nums = array("i",[])

for i in range (0,5):
    num = int(input("Ingrese un número: "))
    nums.append(num)

nums = sorted(nums)
nums.reverse()

print(nums)

    