line1 = ["⬜️","️⬜️","️⬜️"] # a1,b1,c1->
line2 = ["⬜️","⬜️","️⬜️"] # a2,b2,c2->
line3 = ["⬜️️","⬜️️","⬜️️"] # a3,b3,c3->
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input() # Where do you want to put the treasure?
# 🚨 Don't change the code above 👆
# Write your code below this row 👇


row= position[0].lower()

letters = ['a','b','c']

indexletter = letters.index(row)
col = int(position[1])-1



map[col][indexletter]= 'X'


# Write your code above this row 👆
# 🚨 Don't change the code below 👇
print(f"{line1}\n{line2}\n{line3}")