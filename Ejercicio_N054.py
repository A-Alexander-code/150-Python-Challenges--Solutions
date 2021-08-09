import random
moneda1 = ["o","x"]
opcion = random.choice(moneda1)
moneda2 = input("Eliga entre cara(o) o cruz(x)\n")
if moneda2 == opcion:
    print("¡Has ganado!")
else:
    print("Mala suerte :(")
if opcion == "o":
    print("Era cara")
else:
    print("Era cruz")