import math
print("1)Cuadraro\n2)Triangulo")
val = int(input("Selecciona la figura de la que se desea obtener el área\n"))
if val == 1:
    lado = float(input("Ingrese el valor del lado del cuadrado: "))
    a1 = lado**2
    print("El área es igual a",round(a1,2))
elif val == 2:
    h = float(input("Ingrese la altura del triangulo: "))
    b = float(input("Ingrese la base del triangulo: "))
    a2 = 0.5*h*b
    print("El área del triangulo es",round(a2,2))
else:
    print("El valor ingresado no es váido. Intente otra vez")