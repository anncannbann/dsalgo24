# from turtle import Turtle, Screen
#
# print('Making a turtle')
# timmy = Turtle()
# print(timmy)
# timmy.shape('turtle')
# my_screen = Screen()
# timmy.color('DeepPink')
# timmy.forward(100)
# # timmy.left(120)
# # timmy.forward(100)
# # timmy.left(120)
# # timmy.forward(100)
# print(my_screen.candlelight)
# my_screen.exitonclick()


from prettytable import PrettyTable

my_table = PrettyTable()

my_table.add_column('Name', ['a', 'b', 'c', 'l'])
my_table.add_column('Type', ['cute','adorable','sweet','funny'])
my_table.align='l'
print(my_table)
