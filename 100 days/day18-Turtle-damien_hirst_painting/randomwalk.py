from turtle import Turtle, Screen
import random

t = Turtle()
s = Screen()
s.colormode(255)
t.pensize(5)
t.shape("turtle")
t.color('black')
t.fillcolor('BlueViolet')
t.speed('fastest')

angles = [0, 90, 180, 270]

def colors_on():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    tup = (r,g,b)

    return tup


def walk():
    x = 0

    while x < 100:
        #t.pencolor(random.randint(0,255), random.randint(0,255), random.randint(0,255))
        t.color(colors_on())
        choice = random.choice(angles)
        t.right(choice)
        t.forward(random.randint(5, 50))
        x += 1


walk()

screen = Screen()
screen.exitonclick()
