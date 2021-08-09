print("1) Crear un nuevo archivo")
print("2) Mostrar el archivo")
print("3) Añadir un nuevo campo al archivo")
print("Seleccione una de las tres opciones")
qst = int(input("Opción: "))

if qst == 1:
    file = open("Subject.txt","w")
    subj1 = input("Ingrese una asignatura: ")
    subj1 = subj1.lower()
    subj1 = subj1.capitalize()
    file.write(subj1+"\n")
    file.close()
elif qst == 2:
    file = open("Subject.txt","r")
    print(file.read())
    file.close()
elif qst == 3:
    file = open("Subject.txt","a")
    subj2 = input("Ingrese otra asignatura: ")
    subj2 = subj2.lower()
    subj2 = subj2.capitalize()
    file.write(subj2+"\n")
    file.close()
    file = open("Subject.txt","r")
    print(file.read())
    file.close()
else:
    print("¡Error! Ingrese una opción válida")