from array import *
import random

nums1 = array("i",[])
nums2 = array("i",[])

for i in range(0,3):
    num1 = int(input("Ingrese un número: "))
    nums1.append(num1)

for i in range(0,5):
    num2 = random.randint(1,1000)
    nums2.append(num2)

nums1.extend(nums2)
nums1 = sorted(nums1)

for i in nums1:
    print(i)