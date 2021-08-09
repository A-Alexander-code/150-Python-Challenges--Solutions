compnum = 50
cont = 1
guess = int(input("Adivina el número. Prueba ingresando uno\n"))
while guess != compnum:
    if guess < compnum:
        print("El número es muy bajo. Intenta de nuevo")
    else:
        print("El número es muy alto. Intenta de nuevo")
    cont = cont + 1
    guess = int(input("Adivina el número. Prueba ingresando uno\n"))
    
print("¡Has adivinado el número! Te ha tomado",cont,"intentos")