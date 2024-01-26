#heads or tails random
import random
import mymodu



#print(mymodu.pi)
#x = print(10* random.random())


Heads = 1
Tails = 0

toss = random.randint(0,1)
print(f'toss is {toss}')
if toss ==1:
  print('Heads')

else:
  print('Tails')