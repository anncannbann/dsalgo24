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




machine = True

while machine:

    req = input('would you like a latte/espresso/cappuccino?')

    if req == 'latte':
        print(check_resources(req))
        continue
    elif req == 'espresso':
        check_resources(req)
        continue
    elif req == 'cappuccino':
        check_resources(req)
        continue

    elif req == 'report':
        print(resources)
    elif req == 'off':
        machine=False

