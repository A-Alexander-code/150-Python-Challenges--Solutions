import csv

def addtofile():
    file = open("Salaries.csv","a")
    name = input("Ingrese su nombre: ")
    name = name.lower()
    name = name.capitalize()
    salary = float(input("Ingrese su salario: "))
    newRecord = name+","+str(round(salary,2))+"\n"
    file.write(str(newRecord))
    file.close()
    
def view_records():
    file = open("Salaries.csv","r")
    for row in file:
        print(row)
    file.close()

try_again = True
while try_again == True:
    print("1) Add to file")
    print("2) View all records")
    print("3) Quit the program")
    qst = int(input("Enter the number of your selections: "))
    if qst == 1:
        addtofile()
    elif qst == 2:
        view_records()
    elif qst == 3:
        print("The program will close")
        try_again = False
    else:
        print("Incorrect option. Choose again")
