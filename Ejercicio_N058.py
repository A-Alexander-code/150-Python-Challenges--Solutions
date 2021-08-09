import random
num1 = random.randint(1,10)
num2 = random.randint(1,10)
cont = 0

print("Inicia la prueba\nRealice las siguientes operaciones")

oper1 = num1 + num2
oper2 = num1 - num2
oper3 = num1 * num2
oper4 = num1 / num2
oper5 = (num1 + num2) * num1

print("El primer número es: ",num1)
print("El segundo número es: ",num2)

resp1 = int(input("El resultado de sumar el primer y segundo número es \n"))
resp2 = int(input("El resultado de restar el primer y segundo número es \n"))
resp3 = int(input("El resultado de multiplicar el primer y segundo número es \n"))
resp4 = float(input("El resultado de dividir el primer y segundo número es \n"))
print("(",num1,"+",num2,")*",num1)
resp5 = int(input("El resultado de la anterior operación es\n"))

if resp1 == oper1:
    print("Respuesta guarda")
    cont = cont + 1
else:
    print("Respuesta guardada")

if resp2 == oper2:
    print("Respuesta guarda")
    cont = cont + 1
else:
    print("Respuesta guardada")

if resp3 == oper3:
    print("Respuesta guarda")
    cont = cont + 1
else:
    print("Respuesta guardada")

if resp4 == oper4:
    print("Respuesta guarda")
    cont = cont + 1
else:
    print("Respuesta guardada")

if resp5 == oper5:
    print("Respuesta guarda")
    cont = cont + 1
else:
    print("Respuesta guardada")

print("La prueba ha finalizado")
print("Usted ha acertado",cont,"preguntas de 5")