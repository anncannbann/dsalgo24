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

print('''
                        $$\                                             
                        $$ |                                            
$$\  $$\  $$\  $$$$$$\  $$ | $$$$$$$\  $$$$$$\  $$$$$$\$$$$\   $$$$$$\  
$$ | $$ | $$ |$$  __$$\ $$ |$$  _____|$$  __$$\ $$  _$$  _$$\ $$  __$$\ 
$$ | $$ | $$ |$$$$$$$$ |$$ |$$ /      $$ /  $$ |$$ / $$ / $$ |$$$$$$$$ |
$$ | $$ | $$ |$$   ____|$$ |$$ |      $$ |  $$ |$$ | $$ | $$ |$$   ____|
\$$$$$\$$$$  |\$$$$$$$\ $$ |\$$$$$$$\ \$$$$$$  |$$ | $$ | $$ |\$$$$$$$\ 
 \_____\____/  \_______|\__| \_______| \______/ \__| \__| \__| \_______|
                                                                                                                                                                                                  
''')
print('\n\n\n***********************************\n\n\n')
print('Welcome to The Official Rock paper Scissor Game')
user = int(input("Choose your fighter \nEnter 0 for Rock.\nEnter 1 for Paper.\nEnter 2 for Scissors.\n Your input pls" ))
print('\n\n\n***********************************\n\n\n')

options = [rock,paper,scissors]

# rock >scissor
# scissor >paper > rock
computer = random.randint(0,2)
if(user <=3):
    userchose = options[user]
    computerchose = options[computer]
    print(f"u  chose {userchose}")
    print(f"computer chose {computerchose}")
    if computer > user or (computer ==0 and user==2):
        print(f'computer won')

        print('''

                                    $$\                                     
                                    $$ |                                    
$$\   $$\  $$$$$$\  $$\   $$\       $$ | $$$$$$\   $$$$$$$\  $$$$$$\        
$$ |  $$ |$$  __$$\ $$ |  $$ |      $$ |$$  __$$\ $$  _____|$$  __$$\       
$$ |  $$ |$$ /  $$ |$$ |  $$ |      $$ |$$ /  $$ |\$$$$$$\  $$$$$$$$ |      
$$ |  $$ |$$ |  $$ |$$ |  $$ |      $$ |$$ |  $$ | \____$$\ $$   ____|      
\$$$$$$$ |\$$$$$$  |\$$$$$$  |      $$ |\$$$$$$  |$$$$$$$  |\$$$$$$$\       
 \____$$ | \______/  \______/       \__| \______/ \_______/  \_______|      
$$\   $$ |                                                                  
\$$$$$$  |                                                                  
 \______/                                                                   

''')

    elif userchose>computerchose or (user ==0 and computer ==2):
        print('U WON!')
        print('''            88                                                       
            ""              ,d                                       
                            88                                       
8b       d8 88  ,adPPYba, MM88MMM ,adPPYba,  8b,dPPYba, 8b       d8  
`8b     d8' 88 a8"     ""   88   a8"     "8a 88P'   "Y8 `8b     d8'  
 `8b   d8'  88 8b           88   8b       d8 88          `8b   d8'   
  `8b,d8'   88 "8a,   ,aa   88,  "8a,   ,a8" 88           `8b,d8'    
    "8"     88  `"Ybbd8"'   "Y888 `"YbbdP"'  88             Y88'     
                                                            d8'      
                                                           d8'     ''')

    elif userchose ==computerchose:
        print(f"Its a draw")
        print('''
        
      $$\                                  
      $$ |                                 
 $$$$$$$ | $$$$$$\  $$$$$$\  $$\  $$\  $$\ 
$$  __$$ |$$  __$$\ \____$$\ $$ | $$ | $$ |
$$ /  $$ |$$ |  \__|$$$$$$$ |$$ | $$ | $$ |
$$ |  $$ |$$ |     $$  __$$ |$$ | $$ | $$ |
\$$$$$$$ |$$ |     \$$$$$$$ |\$$$$$\$$$$  |
 \_______|\__|      \_______| \_____\____/ 
                                           
                                           
                                           
''')

    else:
        print('Invalid Input')


else:
    print('Invalid input')




