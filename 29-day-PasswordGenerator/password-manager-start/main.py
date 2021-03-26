from tkinter import *
from tkinter import messagebox
from random import choice, shuffle, randint
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
def generate():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []
    [password_list.append(choice(letters)) for _ in range(randint(8, 10))]
    [password_list.append(choice(symbols)) for _ in range(randint(2, 4))]
    [password_list.append(choice(numbers)) for _ in range(randint(2, 4))]

    shuffle(password_list)
    password = ''.join(password_list)

    pass_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Search#
def search():
    web = web_entry.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox._show(message=f"Error")
    else:
        #if web in data
        for k in data.keys():
            if k == web:
                messagebox._show(message=f"web:{k}\nEmail:{data[k]['email']}\nPassword:{data[k]['password']}")
                break
            else:
                messagebox._show(message=f"The record is not found!")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    web = web_entry.get()
    email = email_entry.get()
    password = pass_entry.get()
    new_data = {
        web: {
            "email": email,
            "password": password,
        }
    }

    if web == '' or email == '' or password == '':
        messagebox._show(message="All fields are required!")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)

                web_entry.delete(0, END)
                pass_entry.delete(0, END)
        else:
            data.update(new_data)
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            web_entry.delete(0, END)
            pass_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()

window.title('Password Manager')
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=img)

website = Label(text='Website:')
email = Label(text='Email/Username:')
password = Label(text='Password:')

web_entry = Entry(width=33)
email_entry = Entry(width=52)
pass_entry = Entry(width=33)

email_entry.insert(0, 'stefan.dimitrov.dimitrov@gmail.com')
pass_btn = Button(text='Generate Password', width=15, command=generate)
search_btn = Button(text='Search', width=15, command=search, )
add_btn = Button(text='Add', width=44, command=save)

canvas.grid(row=0, column=1, columnspan=2)

website.grid(column=0, row=1)
email.grid(column=0, row=2)
password.grid(column=0, row=3)

web_entry.grid(column=1, row=1)
email_entry.grid(column=1, row=2, columnspan=2)
pass_entry.grid(column=1, row=3, )

pass_btn.grid(column=2, row=3)
search_btn.grid(column=2, row=1)
add_btn.grid(column=1, row=4, columnspan=2)

web_entry.focus()

window.mainloop()
