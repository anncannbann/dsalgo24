import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇


print('Welcome to The Official Rock paper Scissor Game')
user = int(input("Choose your fighter \nEnter 0 for Rock.\nEnter 1 for Paper.\nEnter 2 for Scissors." ))

options = [rock,paper,scissors]

# rock >scissor
# scissor >paper > rock

computer = random.randint(0,2)
userchose = options[user]
computerchose = options[computer]
print(f"u  chose {userchose}")
print(f"computer chose {computerchose}")




if computer > user or (computer ==0 and user==2):
        print(f'computer won')

elif userchose>computerchose or (user ==0 and computer ==2):
     print('U WON!')

elif userchose ==computerchose:
    print(f"Its a draw")

else:
    print('Invalid Input')
