from tkinter import *

def clicked():
    sel = selectcolour.get()
    window.configure(background = sel)

window = Tk()
window.title("background")
window.geometry("200x200")

selectcolour = StringVar(window)
selectcolour.set("Grey")

colourlist = OptionMenu(window, selectcolour, "Grey", "Red", "Blue", "Green", "Yellow")
colourlist.place(x = 50, y = 30)

clickbtn = Button(text = "Click me", command = clicked)
clickbtn.place(x = 50, y = 150, width = 60, height = 30)

mainloop()

