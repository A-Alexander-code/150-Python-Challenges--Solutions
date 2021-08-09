def ask_num():
    num = int(input("Ingrese un número: "))
    return num

def cuenta(num):
    n = 1
    while n <= num:
        print(n)
        n += 1

def main():
    num = ask_num()
    cuenta(num)

main()