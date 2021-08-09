from tkinter import *

def clicked():
    num = selection.get()
    artref = num + ".gif"
    photo = PhotoImage(file = artref)
    photobox.image = photo
    photobox["image"] = photo
    photobox.update()

window = Tk()
window.title("Art")
window.geometry("400x350")

art = PhotoImage(file = "1.gif")
photobox = Label(window, image = art)
photobox.image = art
photobox.place(x = 100, y = 20, width = 200, height = 150)

selection = Entry(text ="")
selection.place(x = 150, y = 200, width = 100, height = 25)
selection["justify"] = "center"
selection.focus()

button = Button(text = "See art", command = clicked)
button.place(x = 150, y = 250, width = 100, height = 25)

window.mainloop()