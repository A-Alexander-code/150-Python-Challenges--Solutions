import sqlite3

with sqlite3.connect("BookInfo.db") as db:
    cursor = db.cursor()

cursor.execute("SELECT * FROM Books")
for x in cursor.fetchall():
    print(x)

print("-*-*-*-*-*-*-*-*-*-*-")

year = int(input("Enter a date published: "))

print("--/|\(ºmº)/|\--")

cursor.execute("""SELECT Books.Title, Books.DatePublished, Books.Author
FROM Books WHERE DatePublished>? ORDER BY DatePublished""",[year])
for x in cursor.fetchall():
    print(x)

db.close()
