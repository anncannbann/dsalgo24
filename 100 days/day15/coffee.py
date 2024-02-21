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


def coins(res):
    q = int(input('Enter quarters'))
    d = int(input('Enter dimes'))
    n = int(input('Enter nickle'))
    p = int(input('Enter pennies'))
    x = MENU[res]['cost']
    change =0
    total = float((q*0.25)+(d*0.10)+(n * 0.05)+(p * 0.01))
    print(total)

    if total < x:
        return "Sorry that's not enough money. Money refunded."
    elif total > x:
        return f"Here is ${round(total-x,2)} dollars in change.”"
    else:
        return False


def makeCoffee():


machine = True

while machine:

    req = input('would you like a latte/espresso/cappuccino?')
    print(check_resources(req))
    print(coins(req))

    if req == 'latte':
        if not coins(req):
            makeCoffee()
        continue
    elif req == 'espresso':
        continue
    elif req == 'cappuccino':
        continue

    elif req == 'report':
        print(resources)
    elif req == 'off':
        machine=False


