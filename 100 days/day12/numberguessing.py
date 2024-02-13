from random import randint


def game():

    computer = randint(0,100)
    #print(computer)
    lst =[]
    print('Welcome to the Number Guessing Game!')
    print('Im thinking of a number between 1 and 100.')
    level =  input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    
    if(level =='easy'):
        count = 10
    elif (level =='hard'):
        count = 5
    else:
        print('You did not enter a valid response. Goodbye')
        count =0

    print(f"Since you chose {level} level, You have {count} attempts remaining to guess the number.")

    while(count>0):


        guess = int(input('Make a guess: '))
        
        if(guess > computer and guess<100 and guess not in lst):
            print('\nToo High')
            count -=1
            print(f"You have {count} attempts remaining to guess the number.")
            lst.append(guess)
            print(f"You have guessed {lst} so far\n")

        elif computer>guess and guess>0 and guess not in lst:
            print('\nToo Low')
            count -=1
            print(f"You have {count} attempts remaining to guess the number.")
            lst.append(guess)
            print(f"You have guessed {lst} so far\n")

        elif guess <0 or guess >100:
            print('\nBabe, my number is in between 0 an 100.')
            print(f"You have {count} attempts remaining to guess the number.\n")
        
        elif guess in lst:
            print('\nBabe, you already guessed that number, get a grip.')
            print(f"You have {count} attempts remaining to guess the number.\n")
        
        elif guess ==computer:
            print(f"\nYou Guessed it WOOHOO!!!!\n The Answer is {computer}")
            break

    if count==0:
        print(f"\nYou lost  ://///// \n The correct answer was {computer}" )

game()


