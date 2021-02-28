from tkinter import *


def button_clicked():
    miles = input.get()
    result = float(miles)/0.62137
    label3.config(text=f"{result:.2f}")
    label3.config(bg="green")


window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=500, height=300)
window.config(padx=200, pady=200)

label1 = Label(text="Miles", font=("Arial", 15, 'bold'))
label1.grid(row=1, column=3)
label1.config(padx=10, pady=10)
label2 = Label(text="is equal to")
label2.grid(row=2, column=0)
label2.config(padx=10, pady=10)
label3 = Label(text="0",font=("Arial", 10, 'bold'),bg="yellow")
label3.grid(row=2, column=2)
label3.config(padx=10, pady=10)
label4 = Label(text="Km", font=("Arial", 15, 'bold'))
label4.grid(row=2, column=3)
label4.config(padx=10, pady=10)

input = Entry(width=10)
input.grid(row=1, column=2)

button = Button(text="Calculate", font=("Arial", 15), command=button_clicked)
button.grid(row=3, column=2)

window.mainloop()
