from tkinter import *
from tkinter import messagebox
import random
import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

try:
    data = pd.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("./data/listenbg.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def is_known():
    to_learn.remove(current_card)
    data = pd.DataFrame(to_learn)
    data.to_csv("./data/words_to_learn.csv", index = False)
    new_card()


def new_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="English", fill="black")
    canvas.itemconfig(card_word, text=current_card["en"], fill="black")
    canvas.itemconfig(card_color, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(card_title, text="Bulgarian", fill="white")
    canvas.itemconfig(card_word, text=current_card["bg"], fill="white")
    canvas.itemconfig(card_color, image=card_back_img)


window = Tk()
window.title("Flash Card Game")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="./images/card_front.png")
card_back_img = PhotoImage(file="./images/card_back.png")

card_color = canvas.create_image(400, 263, image=card_front_img)

card_title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))

canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)

img_r = PhotoImage(file="./images/wrong.png")
img_a = PhotoImage(file="./images/right.png")

reject_btn = Button(width=100, command=new_card, image=img_r, highlightthickness=0)
approve_btn = Button(width=100, command=is_known, image=img_a, highlightthickness=0)

########## grid ##########
canvas.grid(row=0, column=0, columnspan=2)
reject_btn.grid(row=1, column=1)
approve_btn.grid(row=1, column=0)

new_card()

window.mainloop()
