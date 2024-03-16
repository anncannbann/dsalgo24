from turtle import Turtle, Screen

timmy = Turtle()

timmy.shape("turtle")
timmy.color('black')
timmy.fillcolor('BlueViolet')
# to draw a square
'''
for i in range(0, 4):
    timmy.forward(100)
    timmy.left(90)
'''

for i in range(0,50):
    timmy.forward(5)
    timmy.penup()
    timmy.forward(5)
    timmy.pendown()


screen = Screen()
screen.exitonclick()
