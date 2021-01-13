import random
from turtle import Turtle, Screen

donatelo = Turtle()
donatelo.shape("turtle")
donatelo.pensize(14)
donatelo.forward(30)
donatelo.speed(50)
donatelo.left(90)


list_direction = ["forwards", "backward", "left", "right",]
colors = ["alice blue", "azure2", "Black","Lime","Yellow","Silver","Gray","Maroon","Olive","Green","Purple","Navy"]
direction = [0, 90, 180, 270]

for _ in range(200):
    donatelo.color(random.choice(colors))
    donatelo.forward(30)
    donatelo.setheading(random.choice(direction))


# def move(direction):
#     if direction == "forward":
#         return donatelo.forward(30)
#     elif direction == "backward":
#         return donatelo.backward(30)
#     elif direction == "left":
#         return donatelo.left(90)
#     else:
#         return donatelo.right(90)
#
# for count in range(400):
#     color = random.choice(colors)
#     donatelo.color(color)
#     direction = random.choice(list_direction)
#     move(direction)



screen = Screen()
screen.exitonclick()