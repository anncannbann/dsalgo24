# Write your code below this line 👇

import  math


# Write your code above this line 👆
# Define a function called paint_calc() so the code below works.   

def paint_calc(height,width,cover):

  coverage = 0

  coverage = (height * width) / cover

  print(f"You'll need {math.ceil(coverage)} cans of paint.")
  

# 🚨 Don't change the code below 👇
test_h = int(input()) # Height of wall (m)
test_w = int(input()) # Width of wall (m)
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
