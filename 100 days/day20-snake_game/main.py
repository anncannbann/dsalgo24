from turtle import Turtle, Screen
import random

s = Screen()
s.setup(600, 600)
s.bgcolor('black')
s.title('Snake Game')
s.tracer(0)

snake = []

x = [0, -20, -40]

for i in range(0, 3):
    t = Turtle(shape='square')
    t.penup()
    t.goto(x[i], 0)
    t.color('white', 'purple')
    snake.append(t)

run_snake = True

while run_snake:
    for snack in snake:
        snack.forward(10)


s.exitonclick()
