# Input a list of student scores
student_scores = input().split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])

# Write your code below this row 👇
temp = 0
for scores in student_scores:
  if scores>temp:
    temp=scores
print(f'The highest score in the class is: {temp}')
