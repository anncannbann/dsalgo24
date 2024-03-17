import colorgram

# # Extract 6 colors from an image.
# colors = colorgram.extract('image.jpg', 30)
# rgb =[]
# #print(colors)
#
# for c in colors:
#     r = c.rgb.r
#     g = c.rgb.g
#     b = c.rgb.b
#
#     new_color = (r,g,b)
#
#     rgb.append(new_color)
#
# print(rgb)
from turtle import Turtle, Screen
import random

t = Turtle()
s = Screen()
s.colormode(255)
# t.pensize(5)
t.shape("turtle")
t.color('black')
t.fillcolor('BlueViolet')
t.speed('fastest')

colors_lst = [(246, 245, 243), (233, 239, 246), (132, 166, 205), (221, 148, 106), (32, 42, 61), (199, 135, 148),
              (166, 58, 48), (141, 184, 162), (39, 105, 157), (237, 212, 90), (150, 59, 66), (216, 82, 71),
              (168, 29, 33), (235, 165, 157), (51, 111, 90), (35, 61, 55), (156, 33, 31), (17, 97, 71), (52, 44, 49),
              (230, 161, 166), (170, 188, 221), (57, 51, 48), (184, 103, 113), (32, 60, 109), (105, 126, 159),
              (175, 200, 188), (34, 151, 210), (65, 66, 56)]


def painting():
    for i in range(0, 10):
        t.penup()
        t.dot(20, random.choice(colors_lst))
        t.fd(30)


def damien():
    x = 0
    y = 0

    for i in range(0, 10):
        painting()
        y += 30
        t.setx(x)
        t.sety(y)
        print(t.pos())


damien()
s.exitonclick()
