line1 = ["⬜️","️⬜️","️⬜️"] # a1,b1,c1->
line2 = ["⬜️","⬜️","️⬜️"] # a2,b2,c2->
line3 = ["⬜️️","⬜️️","⬜️️"] # a3,b3,c3->
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input() # Where do you want to put the treasure?
# 🚨 Don't change the code above 👆
# Write your code below this row 👇


row= position[0]
col = int(position[1])-1

if row =='A':
  if col ==0:
    line1[0]='X'
  elif col ==1:
    line2[0] ='X'
  else:
    line3[0] ='X'  
elif row =='B':
  if col ==0:
    line1[1]='X'
  elif col ==1:
    line2[1] ='X'
  else:
    line3[1] ='X' 

elif row =='C':
  if col ==0:
    line1[2]='X'
  elif col ==1:
    line2[2] ='X'
  else:
    line3[2] ='X' 
else:
    row =99




# Write your code above this row 👆
# 🚨 Don't change the code below 👇
print(f"{line1}\n{line2}\n{line3}")