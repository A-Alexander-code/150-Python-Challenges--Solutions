import sqlite3
from tkinter import *

def addartist():
    newname = artistname.get()
    newadress = artistadd.get()
    newtown = artisttown.get()
    newcountry = artistcountry.get()
    newpostcode = artistpostcode.get()
    cursor.execute("""INSERT INTO Artists (nombre,addres,town,country,postcode)
VALUES (?,?,?,?,?)""",(newname,newadress,newtown,newcountry,newpostcode))
    db.commit()
    artistname.delete(0,END)
    artistadd.delete(0,END)
    artisttown.delete(0,END)
    artistcountry.delete(0,END)
    artistpostcode.delete(0,END)
    artistname.focus()

def clearartist():
    artistname.delete(0,END)
    artistadd.delete(0,END)
    artisttown.delete(0,END)
    artistcountry.delete(0,END)
    artistpostcode.delete(0,END)
    artistname.focus()

def addart():
    newartname = artname.get()
    newtitle = arttitle.get()
    newmedium = medium.get()
    newprice = artprice.get()
    cursor.execute("""INSERT INTO Art (artistid, title, medium,price)
VALUES (?,?,?,?)""",(newartname,newtitle,newmedium,newprice))
    db.commit()
    artname.delete(0,END)
    arttitle.delete(0,END)
    medium.set("")
    artprice.delete(0,END)
    artistname.focus()

def clearwindow():
    outputwindow.delete(0,END)

def viewartists():
    cursor.execute("SELECT * FROM Artists")
    for x in cursor.fetchall():
        newrecord = str(x[0])+", "+str(x[1])+", "+str(x[2])+", "+str(x[3])+",  "+str(x[4])+", "+str(x[5])+"\n"
        outputwindow.insert(END,newrecord)

def viewart():
    cursor.execute("SELECT * FROM Art")
    for x in cursor.fetchall():
        newrecord = str(x[0])+", "+str(x[1])+", "+str(x[2])+", "+str(x[3])+",  $"+str(x[4])+"\n"
        outputwindow.insert(END,newrecord)

def searchartistoutput():
    selectedartist = searchartist.get()
    cursor.execute("SELECT nombre FROM Artists WHERE artistid=?",[selectedartist])
    for x in cursor.fetchall():
        outputwindow.insert(END,x)
        cursor.execute("SELECT * FROM Art WHERE artistid=?",[selectedartist])
        for x in cursor.fetchall():
            newrecord = str(x[0])+", "+str(x[1])+", "+str(x[2])+", "+str(x[3])+",  $"+str(x[4])+"\n"
            outputwindow.insert(END,newrecord)
        searchartist.delete(0,END)
        selectedartist.focus()

def searchmediumoutput():
    selectedmedium = medium2.get()
    cursor.execute("""SELECT Art.pieceid, Artists.nombre, Art.medium, Art.price
FROM Artists, Art WHERE Artists.artistid=Art.artistid AND Art.medium=?""",[selectedmedium])
    for x in cursor.fetchall():
        newrecord = str(x[0])+", "+str(x[1])+", "+str(x[2])+", "+str(x[3])+"\n"
        outputwindow.insert(END,newrecord)
    medium2.set("")

def searchbyprice():
    minprice = selectmin.get()
    maxprice = selectmax.get()
    cursor.execute("""SELECT Art.pieceid, Artists.nombre, Art.title, Art.medium, Art.price
FROM Artists,Art WHERE Artists.artistid = Art.artistid AND Art.price >=? AND Art.price<=?""",[minprice,maxprice])
    for x in cursor.fetchall():
        newrecord = str(x[0])+", "+str(x[1])+", "+str(x[2])+", "+str(x[3])+",  $"+str(x[4])+"\n"
        outputwindow.insert(END,newrecord)
    selectmin.delete(0,END)
    selectmax.delete(0,END)
    selectmin.focus()

def sold():
    file = open("SoldArt.txt","a")
    selectedpiece = soldpiece.get()
    cursor.execute("SELECT * FROM Art WHERE pieceid=?",[selectedpiece])
    for x in cursor.fetchall():
        newrecord = str(x[0])+", "+str(x[1])+", "+str(x[2])+", "+str(x[3])+",  $"+str(x[4])+"\n"
        file.write(newrecord)
    file.close()
    cursor.execute("DELETE FROM Art WHERE pieceid=?",[selectedpiece])
    db.commit()

with sqlite3.connect("Art.db") as db:
    cursor = db.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS Artists(
artistid integer PRIMARY KEY,
nombre text,
addres text,
town text,
country text,
postcode text);""")

cursor.execute("""CREATE TABLE IF NOT EXISTS Art(
pieceid integer PRIMARY KEY,
artistid integer,
title text,
medium text,
price integer);""")

window = Tk()
window.title("Art")
window.geometry("1220x600")

title = Label(text = "Enter new artist: ")
title.place(x=10, y=10, width=100, height=25)

artistnamelbl = Label(text = "Name: ")
artistnamelbl.place(x=30, y=40, width=200, height = 25)

artistname = Entry(text ="")
artistname.place(x=110, y=40, width=200, height = 25)
artistname.focus()

artistaddlbl = Label(text = "Address:")
artistaddlbl.place(x=310, y=40, width=80, height = 25)

artistadd = Entry(text ="")
artistadd.place(x=390, y=40, width=200, height = 25)

artisttownlbl = Label(text = "Town:")
artisttownlbl.place(x=590, y=40, width=80, height = 25)

artisttown = Entry(text ="")
artisttown.place(x=670, y=40, width=100, height = 25)

artistcountrylbl = Label(text = "Country:")
artistcountrylbl.place(x=770, y=40, width=80, height=25)

artistcountry = Entry(text ="")
artistcountry.place(x=850, y=40, width=100, height = 25)

artistpostcodelbl = Label(text = "Postcode:")
artistpostcodelbl.place(x=950, y=40, width=80, height = 25)

artistpostcode = Entry(text ="")
artistpostcode.place(x=1030, y=40, width=100, height = 25)

addbtn = Button(text = "Add Artist", command = addartist)
addbtn.place(x=110, y=80, width=130, height = 25)

clearbtn = Button(text = "Clear Artist", command = clearartist)
clearbtn.place(x=250, y=80, width=130, height = 25)

artnamelbl = Label(text = "Artist ID:")
artnamelbl.place(x=30, y=120, width=80, height = 25)

artname = Entry(text ="")
artname.place(x=110, y=120, width=50, height = 25)

artitlelbl = Label(text = "Title:")
artitlelbl.place(x=200, y=120, width=80, height = 25)

arttitle = Entry(text ="")
arttitle.place(x=280, y=120, width=280, height = 25)

artmediumlbl = Label(text = "Medium:")
artmediumlbl.place(x=590, y=120, width=100, height = 25)
medium = StringVar(window)
artmedium = OptionMenu(window, medium, "Oil","Watercolour","Ink","Acrylic")
artmedium.place(x=670, y=120, width=100, height = 25)

artpricelbl = Label(text = "Price:")
artpricelbl.place(x=770, y=120, width=80, height = 25)
artprice = Entry(text ="")
artprice.place(x=850, y=120, width=100, height = 25)

addartbtn = Button(text = "Add Piece", command=addart)
addartbtn.place(x=110, y=150, width=130, height = 25)

clearbtn = Button(text = "Clear Piece", command=addart)
clearbtn.place(x =250, y =150, width=130, height = 25)

outputwindow = Listbox()
outputwindow.place(x=10, y=200, width=1000, height = 350)

clearoutputwindow = Button(text = "Clear Output", command = clearwindow)
clearoutputwindow.place(x=1020, y=200, width=155, height = 25)

viewallartists = Button(text = "View All Artists", command = viewartists)
viewallartists.place(x=1020, y=230, width=155, height=25)

viewallart = Button(text = "View All Art", command = viewart)
viewallart.place(x=1020, y=260, width=155, height = 25)

searchartist = Entry(text ="")
searchartist.place(x=1020, y=300, width=50, height = 25)

searchartistbtn = Button(text = "Search By Artist", command = searchartistoutput)
searchartistbtn.place(x=1075, y=300, width=100, height = 25)

medium2 = StringVar(window)
searchmedium = OptionMenu(window,medium2,"Oil","Watercolour","Ink","Acrylic")
searchmedium.place(x=1020, y=330, width=100, height = 25)

searchmediumbtn = Button(text = "Search", command = searchmediumoutput)
searchmediumbtn.place(x=1125, y=330, width=50, height = 25)

minlbl = Label(text = "Min:")
minlbl.place(x=1020, y=360, width=75, height = 25)

maxlbl = Label(text= "Max:")
maxlbl.place(x=1100, y=360, width=75, height = 25)

selectmin = Entry(text ="")
selectmin.place(x=1020, y=380, width=75, height = 25)

selectmax = Entry(text ="")
selectmax.place(x=1100, y=380, width=75, height = 25)

searchpricebtn = Button(text = "Search by Price", command=searchbyprice)
searchpricebtn.place(x=1020, y=410, width=155, height = 25)

soldpiece = Entry(text ="")
soldpiece.place(x=1020, y=450, width=50, height = 25)

soldbtn = Button(text = "Sold", command = sold)
soldbtn.place(x=1075, y=450, width=100, height = 25)

window.mainloop()
db.close()