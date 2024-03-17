from turtle import Turtle, Screen
import random

t = Turtle()
s = Screen()
s.colormode(255)
#t.pensize(5)
t.shape("turtle")
t.color('black')
t.fillcolor('BlueViolet')
t.speed('fastest')


def colors_on():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    tup = (r, g, b)

    return tup


def spiral():
    x = 0

    while x<100:
        t.color(colors_on())
        t.circle(100)
        t.right(5)
        x += 1

spiral()

s.exitonclick()
