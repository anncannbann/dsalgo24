names = names_string.split(", ")
# The code above converts the input into an array seperating
#each name in the input by a comma and space.
# 🚨 Don't change the code above 👆

import random


n = len(names)
choose = random.randint(0,n-1)

print(f'{names[choose]} is going to buy the meal today!')
