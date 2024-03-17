from turtle import Turtle, Screen
import random

t = Turtle()

t.pensize(3)
t.shape("turtle")
t.color('black')
t.fillcolor('BlueViolet')
t.speed('fastest')
# choices = {'steps': ['t.forward','t.backward','t.left','t.right']}
angles = [0, 90, 180, 270]


def walk():
    x = 0

    while x < 100:
        t.pencolor(random.random(), random.random(), random.random())
        choice = random.choice(angles)
        t.right(choice)
        t.forward(random.randint(5, 50))
        x += 1


walk()

screen = Screen()
screen.exitonclick()
