from turtle import Turtle, Screen
import random

s = Screen()

snake =[]

x = [0,20,40]

for i in range(0,3):
    t = Turtle(shape='square')
    t.goto(x[i],0)
    t.color('white')





s.setup(600,600)
s.bgcolor('black')
s.title('Snake Game')

s.exitonclick()