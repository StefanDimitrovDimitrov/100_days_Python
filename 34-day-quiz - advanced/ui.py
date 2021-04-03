from tkinter import *
from quiz_brain import QuizBrain


THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.score = Label(text="Score:0", bg=THEME_COLOR, fg="white")

        self.canvas = Canvas(width=300, height=250, bd=10, bg="white")
        self.question = self.canvas.create_text(
            150,
            125,
            width= 280,
            text="word",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic")
        )


        self.img_r = PhotoImage(file="./images/false.png")
        self.img_a = PhotoImage(file="./images/true.png")

        self.reject_btn = Button(width=100, command=self.reject, image=self.img_r, highlightthickness=0)
        self.approve_btn = Button(width=100, command=self.approve, image=self.img_a, highlightthickness=0)

        ########## grid ##########
        self.canvas.grid(row=1, column=0, columnspan=2, pady = 50)
        self.reject_btn.grid(row=2, column=1)
        self.approve_btn.grid(row=2, column=0)
        self.score.grid(row=0, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")

        if self.quiz.still_has_questions():
            self.score.config(text=f"Score={self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question, text=q_text)
        else:
            self.canvas.itemconfig(self.question, text=f"The End")
            self.approve_btn.config(state="disabled")
            self.reject_btn.config(state="disabled")


    def reject(self):
        self.give_feedback(self.quiz.check_answer("False"))


    def approve(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.get_next_question)



