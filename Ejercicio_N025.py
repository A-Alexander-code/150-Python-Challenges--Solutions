name = input("Ingrese su nombre: ")
if len(name)<=5:
    surname = input("Ingrese su segundo nombre: ")
    completo = name+surname
    completo = completo.upper()
    print("Su usuario es:",completo)
else:
    name = name.lower()
    print("Su usuarioe es",name)