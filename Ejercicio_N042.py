total = 0
for i in range(0,5):
    num = int(input("Ingrese un número: "))
    var = input("¿Desea incluir el número introducido?\n")
    if var == "si":
        total = total + num
        print("El total de los elementos sumados es",total)
    else:
        num = 0
        print("El número ha sido eliminado de la memoria")