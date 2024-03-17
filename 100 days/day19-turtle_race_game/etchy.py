from turtle import Turtle, Screen

t = Turtle()
s = Screen()
'''
W = Forwards
S = Backwards
A = Counter Clockwise
D = Clockwise
C = Clear
'''


def move_forwards():
    t.forward(10)


def move_back():
    t.back(10)


def cls_screen():
    t.home()
    t.clear()



def counter_clockwise():
    new_heading = t.heading()+10
    t.setheading(new_heading)


def clockwise():
    new_heading = t.heading() - 10
    t.setheading(new_heading)


s.listen()
s.onkey(key="w", fun=move_forwards)
s.onkey(key="a", fun=counter_clockwise)
s.onkey(key="s", fun=move_back)
s.onkey(key="d", fun=clockwise)
s.onkey(key="c", fun=cls_screen)
s.exitonclick()
