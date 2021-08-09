alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q",
            "r","s","t","u","v","w","x","y","z"," "]

def get_data():
    word = input("Ingresa el mensaje: ")
    word = word.lower()
    num = int(input("Ingresa un número (1 - 27): "))
    if num > 27 or num == 0:
        num = int(input("Fuera de rango. Ingresa un número (1 - 27): "))
    data = (word,num)
    return(data)

def make_code(word,num):
    new_word = ""
    for i in word:
        y = alphabet.index(i)
        y += num 
        if y > 27:
            y -= 28
            char = alphabet[y]
            new_word += char
        else:
            char = alphabet[y]
            new_word += char
    print(new_word)
    print("--/|\(ºwº)/|\--")

def decode(word,num):
    new_word = ""
    for i in word:
        y = alphabet.index(i)
        y -= num
        if y < 0:
            y += 28
            char = alphabet[y]
            new_word += char
        else:
            char = alphabet[y]
            new_word += char
    print(new_word)
    print("--/|\(ºwº)/|\--")

def main():
    again = True
    while again == True: 
        print("1) Generar un código") 
        print("2) Decodificar un mensaje")
        print("3) Salir")
        print("-*-*-*-*-*-*--*-*-*-*-*--*-*-*-")
        selection = int(input("Ingrese una opción: "))
        if selection == 1:
            (word,num) = get_data()
            make_code(word,num)
        elif selection == 2:
            (word,num) = get_data()
            decode(word,num)
        elif selection == 3:
            again = False
        else:
            print("Selección no válida")

main()