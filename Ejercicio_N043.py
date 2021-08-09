cuenta = input("¿La cuenta será ascendente (a) o descendente(d)?\n")
if cuenta == "a":
    num1 = int(input("Ingrese un número: "))
    for i in range(0,num1+1):
        print(i)
elif cuenta == "d":
    num2=int(input("Ingrese un número menor a 20: "))
    for i in range(20,num2-1,-1):
        print(i)
else:
    print("El comando no se entiende")