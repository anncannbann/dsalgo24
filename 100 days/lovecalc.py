print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇

namecomb = (name1+name2).lower()

tcnt = namecomb.count('t')
rcnt = namecomb.count('r')
ucnt = namecomb.count('u')
ecnt = namecomb.count('e')
lcnt = namecomb.count('l')
ocnt = namecomb.count('o')
vcnt = namecomb.count('v')
ecnt = namecomb.count('e')


firstdigit = tcnt+rcnt+ucnt+ecnt
secondigit =lcnt+ocnt+vcnt+ecnt
love = int(str(firstdigit)+str(secondigit))

if love <10 or love >90:
  print(f"Your score is {love}, you go together like coke and mentos.")

elif love >40 and love<50:
  print(f'Your score is {love}, you are alright together.')

else:
  print(f'Your score is {love}.')