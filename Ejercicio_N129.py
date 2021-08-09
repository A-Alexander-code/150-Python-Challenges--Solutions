from tkinter import *

def add_number():
    number = number_box.get()
    if number.isdigit():
        number_list.insert(END,number)
        number_box.delete(0,END)
        number_box.focus()
    else: 
        number_box.delete(0,END)
        number_box.focus()

def clear_list():
    number_list.delete(0,END)
    number_box.focus()

window = Tk()
window.title("Number list")
window.geometry("400x200")

label1 = Label(text = "Enter a number:")
label1.place(x = 20, y = 20, width = 100, height = 25)

number_box = Entry(text = 0)
number_box.place(x = 120, y = 20, width = 100, height = 25)
number_box.focus()

button1 = Button(text = "Add to list", command = add_number)
button1.place(x = 250, y = 20, width = 100, height = 25)

number_list = Listbox()
number_list.place(x =120, y = 50, width = 100, height = 100)

button2 = Button(text = "Clear list", command = clear_list)
button2.place(x =250, y = 50, width = 100, height = 25)

window.mainloop()