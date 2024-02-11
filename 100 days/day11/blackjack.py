#blackjack game

import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_a_card():
    deal =random.choice(cards)
    print(deal)
    return deal

def add(comp,user):
    comp_sum=0
    user_sum = 0
    for card in comp:
        comp_sum += card

    for card in user:
        user_sum += card
    return comp_sum,user_sum

def checkwinner(comp_sum,user_sum,comp):
    while comp_sum <17:
        deal =random.choice(cards)
        comp.append(deal)
        comp_sum+=deal

    print(comp)
    
    if comp_sum >17 and comp_sum <21:
        if comp_sum> user_sum:
            print("Comp won, you lose")
        elif user_sum > comp_sum and user_sum <21:
            print("YOU WON!!!")
    if user_sum >21:
        print('you lose')



def blackjack():
    comp=[]
    user=[]
    deal_a_card(comp,user)
    comp_score,user_score = add(comp,user)
    print(f"Computer's first card :{comp[0]}")
    print(f" You have :{user}, current score {user_score}")
    choice = True
    toContinue = input('Do you want to continue y for yes and n for no').lower()

    while choice:
        if toContinue =='n':
            x,y =add(comp,user)
            checkwinner(x,y,comp)
            choice = False
        else:
            print('Dealing you a card')
            deal_a_card(comp,user)
            break




    




user = input("do you want to play a game of blackjack? \n Type y for yes and n for no").lower()

if user=="y":
    blackjack()

else:
    print('Goodbye')