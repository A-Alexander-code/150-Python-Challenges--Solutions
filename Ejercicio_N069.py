paises =("Ecuador","Colombia","Perú","Venezuela","Chile")
print(paises)
pos = input("Ingrese uno de los países: ")
pos = pos.capitalize()

for i in paises:
    if pos == i:
        print("La información se encuentra asignada en la posición",paises.index(i))
    else:
        break

print("Error. No se encuentra dentro del banco de datos")