#blackjack game

import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_a_card():
    deal =random.choice(cards)
    #print(deal)
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

    print(f"comp has {comp}")
    
    if comp_sum >17 and comp_sum <21:
        if comp_sum> user_sum:
            print(f"Comp won {comp_sum}, you lose {user_sum}")
        elif user_sum > comp_sum and user_sum <21:
            print(f"YOU WON!!!urs: {user_sum},computers : {comp_sum}")
    if user_sum >21:
        print(f"Comp won {comp_sum}, you lose {user_sum}")



def blackjack():
    comp=[]
    user=[]
    for i in range(0,2):
        user_deal= deal_a_card()
        user.append(user_deal)
    for i in range(0,2):
        comp_deal =deal_a_card()
        comp.append(comp_deal)
    
    comp_score,user_score = add(comp,user)
    if comp_score ==21:
        print(f"YOU lose !!!urs: {user_score},computers : {comp_score}")
    elif user_score ==21:
        print(f"YOU WON!!!urs: {user_score},computers : {comp_score}")
    
    elif user_score>21:
        for card in user:
            if card ==11:
                card =1
        add(comp,user)
        if user_score > 21:
            print('You lose')
            
    else:

        print(f"Computer's first card :{comp}, current score {comp_score}")
        print(f" You have :{user}, current score {user_score}")
        choice = True
     

        while choice:
            toContinue = input('Do you want to continue y for yes and n for no').lower()
            if toContinue =='n':
                x,y =add(comp,user)
                checkwinner(x,y,comp)
                choice = False
            else:
                print('Dealing you a card')
                card_dealt =deal_a_card()
                user.append(card_dealt)
                print(f'Your new cards {user}')
                x,y =add(comp,user)


            



            


user = input("do you want to play a game of blackjack? \n Type y for yes and n for no").lower()

if user=="y":
    blackjack()

else:
    print('Goodbye')