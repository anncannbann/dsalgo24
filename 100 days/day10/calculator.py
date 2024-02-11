logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""


#print(logo)


def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    print('mul')
    return a*b


def div(a,b):
    print('dividing')
    return a/b

#making a dict
operations ={
     '+':add,
     '-':sub ,
     '*':mul,
     '/':div
 }

a = int(input("first number : "))

for key in operations:
    print(key)

user_op = input("Enter the symbol")
b= int(input("second number : "))

function1 = operations[user_op]
answer = function1(a,b)

print(f'{a}{user_op}{b}={answer} ')
user_op = input("Enter the symbol")
c= int(input("next number : "))

function1 = operations[user_op]
second = function1(answer,c)

print(f'{answer}{user_op}{c}={second} ')