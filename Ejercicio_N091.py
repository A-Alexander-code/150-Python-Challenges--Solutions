from array import *

nums = array("i",[12,78,96,78,37])
print(nums)

num = int(input("Ingrese uno de los número de la matriz mostrada: "))

if nums.count(num) == 1:
    print("El número aparece una sola vez")
else:
    rep = nums.count(num)
    print("El número",num,"aparece",rep,"veces en la matriz")