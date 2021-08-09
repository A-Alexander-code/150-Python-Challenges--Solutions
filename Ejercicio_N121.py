def add_names():
    new_name = input("Enter new name: ")
    names.append(new_name)
    return names

def change_names():
    for i in range(0,len(names)):
        display = i, names[i]
        print(display)
    index = int(input("Choose the index name: "))
    new_name = input("Enter a new name: ")
    names[index] = new_name
    return names

def delete_names():
    for i in range(0,len(names)):
        display = i, names[i]
        print(display)
    index = int(input("Choose the index name: "))
    del names[index]
    return names


def view_names():
    for i in range(0,len(names)):
        display = i, names[i]
        print(display)

def main():
    try_again = True
    while try_again == True:
            print("1) Add name to the list")
            print("2) Change name in the list")
            print("3) Delete neme in the list")
            print("4) Show list")
            print("5) Exit")
            selection = int(input("Choose one of the following options: "))
            if selection == 1:
                names = add_names()
            elif  selection == 2:
                names = change_names()
            elif selection == 3:
                names = delete_names()
            elif selection == 4:
                names = view_names()
            elif selection == 5:
                try_again = False
            else:
                print("Incorrect option. Choose again: ")
            data = (names,try_again)

names = []
main()