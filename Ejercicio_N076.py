per01 = input("Ingrese el nombre del primer invitado: ")
per01 = per01.capitalize()
per02 = input("Ingrese el nombre del primer invitado: ")
per02 = per02.capitalize()
per03 = input("Ingrese el nombre del primer invitado: ")
per03 = per03.capitalize()
invitados = [per01,per02,per03]
qst = "s"
while qst == "s":
    qst = input("¿Desea invitar más personas? (s)/(n) ")
    if qst == "s":
        per = input("Ingrese el nombre del siguiente invitado: ")
        per = per.capitalize()
        invitados.append(per)
    else:
        break
print("Usted ha invitado a",len(invitados),"personas a la fiesta")