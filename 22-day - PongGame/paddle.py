from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()

        self.shape("square")
        self.color("orange")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(position)


    def up(self):
        new_y = self.ycor() + 50
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 50
        self.goto(self.xcor(), new_y)

