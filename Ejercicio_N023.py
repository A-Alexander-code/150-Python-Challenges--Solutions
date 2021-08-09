texto = input("Escribe una parte de una canción: ")
tlen = len(texto)
print("La longitud de la frase es de:",tlen,"carácteres")
num1 = int(input("Ingresa un número menor a la longitud incluido el 0: "))
num2 = int(input("Ingresa un número igual o menor a la longitud: "))
parte = texto[num1:num2]
print("La fracción extraída es: ",parte)