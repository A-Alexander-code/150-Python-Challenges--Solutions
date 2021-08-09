import math
r = float(input("Ingrese el radio del cilindro: "))
h = float(input("Ingrese la altura del cilindro: ")) 
vol = round(math.pi*(r**2)*h,3)
print("El volumen del cilindro es",vol,"unidades^3")