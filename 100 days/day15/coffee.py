MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
profit = 0
resources = {

    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def check_resources(res):
    x = MENU[res]['ingredients']
    #print(x)
    if resources['water'] < x['water'] or resources['milk'] < x['milk'] or resources['coffee'] < x['coffee']:
        return False

    else:
        return True


def make_coffee(res):
    x = MENU[res]['ingredients']
    resources['water'] -= x['water']
    resources['milk'] -= x['milk']
    resources['coffee'] -= x['coffee']
    return f'Here is your {res} ☕️.'


def coins(res):
    q = int(input('Enter quarters'))
    d = int(input('Enter dimes'))
    n = int(input('Enter nickle'))
    p = int(input('Enter pennies'))
    x = MENU[res]['cost']

    total = float((q * 0.25) + (d * 0.10) + (n * 0.05) + (p * 0.01))
    change = round(total - x, 2)
    #print(f"You gave ${total}")

    if total < x:
        return "Sorry that's not enough money. Money refunded."
    elif total > x:

        print(make_coffee(res))
        global profit
        profit += x
        return f"Here is ${change} dollars in change."

    else:
        return "No change need, exact amount given."


machine = True

while machine:

    req = input('would you like a latte/espresso/cappuccino?')
    if req == 'report':
        print(resources)
        print(f"Total profit of the day {profit}")

    elif req == 'off':
        machine = False
    else:

        res = check_resources(req)
        if res:
            cost = coins(req)
            print(cost)
        else:
            print('Sorry insufficient resources, please try again later.')
            machine = False
