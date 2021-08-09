import sqlite3

with sqlite3.connect("PhoneBook.db") as db:
    cursor = db.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS Names(
id integer PRIMARY KEY,
firstname text,
surname text,
phone_number text); """)

cursor.execute(""" INSERT INTO Names(id, firstname, surname, phone_number)
VALUES("1","Simon","Howels","01223 349762")""")
db.commit()

cursor.execute(""" INSERT INTO Names(id, firstname, surname, phone_number)
VALUES("2","Karen","Phillips","01954 295773")""")
db.commit()

cursor.execute(""" INSERT INTO Names(id, firstname, surname, phone_number)
VALUES("3","Darren","Smith","01583 749012")""")
db.commit()

cursor.execute(""" INSERT INTO Names(id, firstname, surname, phone_number)
VALUES("4","Anne","Jones","01323 567322")""")
db.commit()

cursor.execute(""" INSERT INTO Names(id, firstname, surname, phone_number)
VALUES("5","Mark","Smith","01223 855534")""")
db.commit()


db.close()
