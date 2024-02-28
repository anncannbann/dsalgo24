from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
#menu_item = MenuItem()
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
is_on = True

while is_on:
    options = menu.get_items()
    choice = input(f'Enter your choice {options}')

    if choice == 'report':
        coffee_maker.report()
        money_machine.report()
    elif choice == 'off':
        is_on = False
    else:
        x = menu.find_drink(choice)

keyword