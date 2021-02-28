from tkinter import *


def button_clicked():
    my_label["text"] = input.get()
    # my_label.config(text = "Something")


window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

my_label = Label(text="I am a Label", font=("Arial", 24, 'bold'))
my_label.grid(row=0, column=0)

button = Button(text="Button", command=button_clicked)
button.grid(row=1, column=1)

button2 = Button(text="New Button", command=button_clicked)
button2.grid(row=0, column=3)

input = Entry(width=10)
input.grid(row=3, column=4)

window.mainloop()
