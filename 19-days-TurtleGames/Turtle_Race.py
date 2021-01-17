from turtle import Turtle, Screen
import random


is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet Sofia", prompt="Which turtle will min the race? Enter a color: ")
user_bet2 = screen.textinput(title="Make your bet Stefan", prompt="Which turtle will min the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_position = [-100, -60, -20, 20, 60, 100]
all_turtles = []


for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=-y_position[turtle_index])
    all_turtles.append(new_turtle)

if user_bet and user_bet2:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet and winning_color == user_bet2:
                print(f"Sofia and Stefan win! The {winning_color} turtle is the winner")
            elif winning_color == user_bet:
                print(f"Sofia win!The {winning_color} turtle is the winner")
            elif winning_color == user_bet2:
                print(f"Stefan win!The {winning_color} turtle is the winner")
            else:
                print(f"The game is draw. The {winning_color} turtle is the winner!")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()
