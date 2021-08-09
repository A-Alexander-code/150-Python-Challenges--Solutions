import sqlite3

def viewphonebook():
    cursor.execute("SELECT * FROM Names")
    for x in cursor.fetchall():
        print(x)

def addphonebook():
    newID = input("Enter ID number: ")
    newfirstname = input("Enter first name: ")
    newsurname = input("Enter surname: ")
    newphonenumber = input("Enter phone number: ")
    cursor.execute("""INSERT INTO Names(id, firstname,surname,phone_number)
VALUES(?,?,?,?)""",(newID,newfirstname,newsurname,newphonenumber))
    db.commit()

def searchsurname():
    whichSurname = input("Enter a surname: ")
    cursor.execute("SELECT * FROM Names WHERE surname=?",[whichSurname])
    for x in cursor.fetchall():
        print(x)

def deletename():
    selectid = int(input("Enter id: "))
    cursor.execute("DELETE FROM Names WHERE id = ?",[selectid])
    cursor.execute("SELECT * FROM Names")
    for x in cursor.fetchall():
        print(x)
    db.commit()

with sqlite3.connect("PhoneBook.db") as db:
    cursor = db.cursor()

def main():
    retry = True
    while retry == True:
        print("-*-*-*-*-*-*-*-*-*-*-")
        print("Main Menu")
        print("1) View phone book")
        print("2) Add to phone book")
        print("3) Search for surname")
        print("4) Delete person from phone book")
        print("5) Quit")
        print("--/|\(ºwº)/|\--")
        selection = input("Enter your selction: ")
        if selection == "1":
            viewphonebook()
        elif selection == "2":
            addphonebook()
        elif selection == "3":
            searchsurname()
        elif selection == "4":
            deletename()
        elif selection == "5":
            retry = False
        else:
            print("Incorrect selection entered")

main()
db.close()