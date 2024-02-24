from turtle import Turtle, Screen

print('Making a turtle')
timmy = Turtle()
print(timmy)
timmy.shape('turtle')
my_screen = Screen()
timmy.color('DeepPink')
timmy.forward(100)
# timmy.left(120)
# timmy.forward(100)
# timmy.left(120)
# timmy.forward(100)
print(my_screen.canvheight)

my_screen.exitonclick()