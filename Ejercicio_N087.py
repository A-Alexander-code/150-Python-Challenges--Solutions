word = input("Ingrese una palabra: ")
longitud = len(word)
num = 1

for letter in word:
    position = longitud - num
    letter = word[position]
    num = num + 1
    print(letter)