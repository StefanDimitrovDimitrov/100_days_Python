import colorgram
import random
import turtle as t

colors = colorgram.extract("untitled.jpg", 150)

color_list = []

for i in range(len(colors)):
    first_color = colors[i]
    rgb = tuple(first_color.rgb)
    color_list.append(rgb)

t.colormode(255)

hirst = t.Turtle()
hirst.speed("slow")
hirst.shape("turtle")
hirst.penup()
hirst.setpos(200.00, -300.00)
hirst.down()

dote_size = 20
distance = 50

def turn_turtle_left():
    hirst.penup()
    hirst.left(90)
    hirst.forward(distance)
    hirst.left(90)
    hirst.down()

def turn_turtle_right():
    hirst.penup()
    hirst.right(90)
    hirst.forward(distance)
    hirst.right(90)
    hirst.down()

def turtle_painting():
    hirst.color(random.choice(color_list[3:]))
    hirst.dot(dote_size)
    hirst.penup()
    hirst.forward(distance)
    hirst.down()
    hirst.color(random.choice(color_list[3:]))
    hirst.dot(dote_size)

for x in range(10):
    if x % 2 == 0:
        turn_turtle_left()
    else:
        turn_turtle_right()
    for y in range(10):
        turtle_painting()

hirst.ht()





screen = t.Screen()
screen.exitonclick()