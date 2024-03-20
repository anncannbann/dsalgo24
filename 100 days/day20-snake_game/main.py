from turtle import Turtle, Screen
import random
import time

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

s.update()
run_snake = True

while run_snake:
    s.update()
    time.sleep(0.1)

    for snacks in range(len(snake)-1,0,-1):
        new_x = snake[snacks -1].xcor()
        new_y = snake[snacks - 1].ycor()
        snake[snacks].goto(new_x,new_y)
    snake[0].forward(20)

s.exitonclick()
