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


userchose = options[user]

computerchose = options[random.randint(0,2)]
print(f"u  chose {userchose}")
print(f"computer chose {computerchose}")

if userchose ==computerchose:
    print(f"Its a draw")


