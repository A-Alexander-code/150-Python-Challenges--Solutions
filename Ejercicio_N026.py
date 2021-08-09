palabra = input("Ingrese una palabra a ser traducida: ")
letra_01 = palabra[0]
longitud = len(palabra)
resto = palabra[1:longitud]
if letra_01 != "a" and letra_01 != "e" and letra_01 != "i" and letra_01 != "o" and letra_01 != "u":
    trad01 = resto+letra_01+"ay"
    print("La equivalencia es:",trad01)
else:
    trad02 = palabra+"way"
    print("La equivalencia es:",trad02) 