import random

print("El primer número debe ser menor que el segundo número")
def random_num():
    num01 = int(input("Ingrese un número: "))
    num02 = int(input("Ingrese otro número: "))
    comp_num = random.randint(num01,num02)
    return comp_num

def guess():
    print("Estoy pensando en un número... ")
    num03 = int(input("¿Cuál es el número en el que pienso?\n"))
    return num03

def check_answer(comp_num,num03):
    try_again = True
    while try_again == True:
        if comp_num == num03:
            print("¡Correcto! Tú ganas") 
            try_again == False
            break
        elif comp_num > num03:
            num03 = int(input("Muy bajo. Intenta otra vez: "))
        else:
            num03 = int(input("Muy alto. Intenta otra vez: "))


def main():
    comp_num = random_num()
    num03 = guess()
    check_answer(comp_num,num03)

main()