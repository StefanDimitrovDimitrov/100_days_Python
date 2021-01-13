from turtle import Turtle, Screen


timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("purple")

#
# for _ in range(4):
#     timmy_the_turtle.left(90)
#     timmy_the_turtle.forward(100)

# def draw(space, x):
#     for i in range(x):
#         for j in range(x):
#             # dot
#             timmy_the_turtle.dot(5)
#
#             # distance for another dot
#             timmy_the_turtle.forward(space)
#         timmy_the_turtle.backward(space * x)
#
#         # direction
#         timmy_the_turtle.right(90)
#         timmy_the_turtle.forward(space)
#         timmy_the_turtle.left(90)
#
#     # Main Section
#
#
# timmy_the_turtle.penup()
# draw(10, 10)
#
# for _ in range(10):
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.penup()
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.down()
# colors = ["orange1","purple","gray","black","blue","red","yellow"]
# angle = 3
# for index in range(6):
#     timmy_the_turtle.color(colors[index])
#     for _ in range(angle):
#         timmy_the_turtle.forward(100)
#         timmy_the_turtle.right(360/angle)
#     angle += 1

timmy_the_turtle.dot(50)

screen = Screen()
screen.exitonclick()