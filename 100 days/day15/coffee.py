MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
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
    print(x)
    if resources['water'] < x['water'] or resources['milk'] < x['milk'] or resources['coffee'] < x['coffee']:
        return 'Sorry insufficient resources, please try again later.'

    else:
        return True

def make_coffee(res):
    x = MENU[res]['ingredients']
    resources['water'] -= x['water']
    resources['milk'] -= x['milk']
    resources['coffee'] -= x['coffee']
    print('Here is your coffee')


def coins(res):
    q = int(input('Enter quarters'))
    d = int(input('Enter dimes'))
    n = int(input('Enter nickle'))
    p = int(input('Enter pennies'))
    x = MENU[res]['cost']

    total = float((q*0.25)+(d*0.10)+(n * 0.05)+(p * 0.01))
    change = round(total-x,2)
    print(total)

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
        print(profit)
    else:

        res = check_resources(req)
        if res:
            cost = coins(req)
        else:
            print(coins(req))
            machine = False

        if req == 'off':
            machine=False


