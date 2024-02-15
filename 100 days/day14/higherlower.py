from gamedata import data
import random



#generate 
def generate():

    x = random.choice(data)
    #print(x)
    return x


# game
def game():
    A = generate()
    B = generate()

    print(A)
          #,'description','country'])
    #print(B['name','description','country'])

    count = 0

    loo =True
    while loo:

        choice =input('Which one is greater A or B').lower()
        print(f"A is {A}\n B is {B}")
        if A ==B:
            print('same')
            A =generate()
        
        if A['follower_count'] > B['follower_count']:
            if choice =='a':
                count+=1
                print(f"You're right! Current score: {count}.")
                A= B
                B = generate()
            elif choice =='b':
                print(f"Sorry, that's wrong. Final score: {count}")
                loo =False
    
        elif B['follower_count'] > A['follower_count']:
            if choice =='b':
                count+=1
                print(f"You're right! Current score: {count}.")
                A = B
                B = generate()
            elif choice =='a':
                print(f"Sorry, that's wrong. Final score: {count}")
                loo = False







#swap


#finalscore



print(generate())
print(game())