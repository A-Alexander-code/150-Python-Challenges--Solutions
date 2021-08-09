num1 = int(input("Ingrese el 1er número: "))
num2 = int(input("Ingrese el 2do número: "))
num3 = 0
qst = "s"
while qst == "s":
    valor = int(input("Ingrese el siguiente número: "))
    num3 = num3 + valor
    qst = input("¿Desea ingresar otro número? (s/n)\n")

total = num1 + num2 + num3
print("El valor final es",total)