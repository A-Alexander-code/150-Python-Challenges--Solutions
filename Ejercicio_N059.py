import random
colores = ["azul","verde","amarillo","rojo","morado"]
print(colores)
rcolor = random.choice(colores)
intento = True
while intento == True:
    resp = input("Ingresa un color de la lista\n")
    resp = resp.lower()
    if resp == rcolor:
        print("¡Buen Trabajo!") 
        intento = False
    else:
        if rcolor == "azul":
            print("Es lo que tienen en común el cielo y el mar")
        elif rcolor == "verde":
            print("La naturaleza se viste con ese color")
        elif rcolor == "amarillo":
            print("¿No tienes ganas de una banana?")
        elif rcolor == "rojo":
            print("El tono de las rosas")
        elif rcolor == "morado":
            print("Las uvas son de ese color")