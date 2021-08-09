nums = []
pos = 0

while pos < 3:
    num = int(input("Igrese un número: "))
    nums.append(num)
    print(nums)
    pos = pos + 1

lastnum = input("¿Desea guardar el último número ingresado? (s/n)\n")

if lastnum == "n":
    nums.remove(num)

print(nums)