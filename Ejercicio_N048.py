inv = "s"
cont = 0
while inv == "s":
    nom = input("Ingrese el nombre de la persona invitada\n")
    cont = cont + 1
    inv = input("¿Desea invitar a otra persona? (s/n)\n")

print("La cantidad de persona invitadas es",cont)
