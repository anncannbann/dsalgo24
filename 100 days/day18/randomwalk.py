from turtle import Turtle, Screen
import random

t = Turtle()

t.pensize(5)
t.shape("turtle")
t.color('black')
t.fillcolor('BlueViolet')

choices = ['forward()','backward()','left()','right()']

def walk():

    x = 0

    while x<20:
        t.pencolor(random.random(), random.random(), random.random())
        move = random.choice(choices)
        move()
        x+=1


walk()

screen = Screen()
screen.exitonclick()
