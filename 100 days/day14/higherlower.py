from gamedata import data
from art import logo,vs
import random
import os

clear = lambda: os.system('clear')


#generate 
def generate():

    x = random.choice(data)
    #print(x)
    return x


# game
def game():
    A = generate()
    B = generate()


    count = 0

    loo =True
    while loo:
        if A ==B:
            B = generate()
        print(f"A is {A['name'],A['description'],A['country']}\n")

        print(vs)

        print(f"\nB is {B['name'],B['description'],B['country']}")
        
        choice =input("Who has more followers? Type 'A or a' or 'B or b': ").lower()


        
        if A['follower_count'] > B['follower_count'] and choice =='a':
            count+=1
            print(f"You're right! Current score: {count}.")
            clear()
            A= B
            B = generate()
    
        elif B['follower_count'] > A['follower_count'] and choice =='b': 
            count+=1
            print(f"You're right! Current score: {count}.")
            clear()
            A = B
            B = generate()
        else:
                print(f"\n\nSorry, that's wrong. Final score: {count}")
                loo = False




print(logo)

game()