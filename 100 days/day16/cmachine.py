from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
menu_item = MenuItem()
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
is_on = True

while is_on:
    options = menu.get_items()

    x = menu.find_drink(options)
    print(x)

    if options == 'report':
        coffee_maker.report()
        money_machine.report()
    elif options == 'off':
        is_on = False
    else:
        print('hello')
        is_on = False
