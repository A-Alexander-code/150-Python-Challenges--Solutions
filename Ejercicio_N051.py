num = 10
rest = 9
while num > 0:
    print("Hay",num,"botella verdes colgadas en la pared\n",num,
          "botellas colgando de la pared\n","Y si 1 botella accidentalmente cayera")
    ask = int(input("¿Cuántas botellas sobran?\n"))
    if ask == rest:
        num = num - 1
    else:
        print("No. Intenta de nuevo")
    rest = rest - 1

print("Ya no restan botella en la pared")    