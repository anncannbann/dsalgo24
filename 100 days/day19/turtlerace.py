from turtle import Turtle, Screen
import random

'''
Turtle Race
'''
# screen stuff
s = Screen()
s.colormode(255)
s.setup(width=500, height=400)
s.title("Welcome to the turtle Race!")

# preset data
race_on = False
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
index = [-90, -60, -30, 0, 30, 60]
all_turtles = []

# initialising 6 turtles , giving them index and colors
for t in range(0, 6):
    t1 = Turtle(shape='turtle')
    t1.penup()
    t1.goto(-230, index[t])
    t1.color(colors[t])
    all_turtles.append(t1)

# opens a window to place your bet
bet = s.textinput(title="Make your Bet", prompt="Enter the color you think will win!!!:")

# race begins here
if bet:
    race_on = True

while race_on:

    for turtle in all_turtles:

        if turtle.xcor() > 230:
            race_on = False
            winning_color = turtle.pencolor()
            if winning_color == bet:
                print(f"You won ! {winning_color} is the winner")
            else:
                print(f"You Lost ! {winning_color} is the winner")

        dist = random.randint(1, 10)
        turtle.forward(dist)

s.exitonclick()
