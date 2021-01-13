
import turtle as t
import random

spiro = t.Turtle()
t.colormode(255)
spiro.shape("turtle")
spiro.speed("fastest")

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    return(r, g, b)

def draw_spirograph(size_of_gap):
    for _ in range(int(360/ size_of_gap)):
        spiro.color(random_color())
        spiro.circle(100)
        spiro.forward(2)
        spiro.setheading(spiro.heading() + size_of_gap)

draw_spirograph(4)





screen = t.Screen()
screen.exitonclick()