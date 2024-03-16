from turtle import Turtle, Screen
import random

t = Turtle()


t.pensize(5)
t.shape("turtle")
t.color('black')
t.fillcolor('BlueViolet')

n = 3

while n < 10:
    angle = 360 / n
    t.pencolor(random.random(), random.random(), random.random())
    for i in range(n):

        t.forward(30)
        t.right(angle)
        t.forward(30)
    n += 1


screen = Screen()
screen.exitonclick()
