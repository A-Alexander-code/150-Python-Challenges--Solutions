import sqlite3

with sqlite3.connect("BookInfo.db") as db:
    cursor = db.cursor()

cursor.execute("SELECT * FROM Authors")
for x in cursor.fetchall():
    print(x)

print("-*-*-*-*-*-*-*-*-*-*-")

AuthorsName = input("Enter a Author's name: ")

print("--/|\(ºwº)/|\--")

cursor.execute("""SELECT * FROM Books WHERE Books.Author=?""",[AuthorsName])
for x in cursor.fetchall():
    newrecord = str(x[0])+" - "+str(x[1])+" - "+str(x[2])+" - "+str(x[3])+"\n"
    file = open("BooksbyAuthor.csv","a")
    file.write(newrecord)
    file.close

db.close()