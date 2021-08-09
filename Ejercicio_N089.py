from array import *
import random

nums = array("i",[])
cont = 0

while cont < 5:   #También puede ser realizad con: <<for i in range (0,5):>>
    num = random.randint(-32768,32767)
    nums.append(num)
    cont = cont + 1

for i in nums:
    print(i)