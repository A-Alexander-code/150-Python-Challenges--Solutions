import sqlite3

with sqlite3.connect("BookInfo.db") as db:
    cursor = db.cursor()

cursor.execute("SELECT * FROM Authors")
for x in cursor.fetchall():
    print(x)

print("-*-*-*-*-*-*-*-*-*-*-")

location = input("Enter a place of birth: ")
location = location.lower()
location = location.capitalize()

print("--/|\(ºwº)/|\--")

cursor.execute("""SELECT Books.Title, Books.Author, Books.DatePublished, Authors.placeOfBirth
FROM Books,Authors WHERE Authors.Name=Books.Author AND Authors.placeOfBirth =?""",[location])
for x in cursor.fetchall():
    print(x)
    
db.close()