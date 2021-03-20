from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 1
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text = '00:00')
    my_label.config(text='Timer')
    check_markers.config(text="")
    global reps
    reps = 1
    button_start["state"] = "active"

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    button_start["state"] = "disable"
    if reps % 2 != 0:
        count_down(work_sec)
        my_label.config(text='Work', fg=GREEN)
        reps+=1
    elif reps % 2 == 0 and reps % 4 != 0:
        count_down(short_break_sec)
        my_label.config(text='Break', fg=PINK)
        reps += 1
    else:
        count_down(long_break_sec)
        my_label.config(text='Break', fg=RED)
        reps += 1
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):

    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ''
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✔"
        check_markers.config(text=marks)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg=YELLOW)


canvas = Canvas(width=200, height=225, bg=YELLOW, highlightthickness=0)
img = PhotoImage(file='tomato.png')
fb = GREEN
canvas.create_image(100, 112, image=img)
timer_text = canvas.create_text(100, 130, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(row=1, column=1)
my_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
my_label.grid(row=0, column=1)


button_start = Button(text="Start", command=start_timer, highlightthickness=0)
button_start.grid(row=3, column=0)

button_reset = Button(text="Reset", command=reset, highlightthickness=0)
button_reset.grid(row=3, column=3)
check_markers = Label(text="✔", fg=GREEN, bg=YELLOW)
check_markers.grid(row=3, column=1)
window.mainloop()

window.mainloop()
