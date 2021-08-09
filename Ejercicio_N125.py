from tkinter import *
import random

def click():
    num = random.randint(1,6)
    answer["text"] = num

window = Tk()
window.title("Dice - Dice")
window.geometry("100x120")

button1 = Button(text = "Test your luke!", command = click)
button1.place(x = 20, y = 45, width = 80, height = 20)

answer = Message(text = "")
answer.place(x = 40, y = 80, width = 40, height = 20)

window.mainloop()