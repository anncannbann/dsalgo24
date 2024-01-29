# Input a Python list of student heights
student_heights = input().split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


avg_ht = 0
cnt=0

for height in student_heights:
  avg_ht+=height
  cnt+=1

x= round(avg_ht/cnt)

print(f"total height = {avg_ht}")
print(f"number of students = {cnt}")
print(f"average height = {x}")

  
# Write your code below this row 👇
