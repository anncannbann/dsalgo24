def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
        print("Leap year")
      else:
        return False
        print("Not leap year")
    else:
      return True
      print("Leap year")
  else:
    return False
    print("Not leap year")
  
# TODO: Add more code here 👇
def days_in_month(year,month):
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 
  x = is_leap(year)
  #print(x)
  if x==True:
    if month ==2:
      #print (month_days[month-1]+1)
      return month_days[month-1]+1
  return month_days[month-1]
    

  
#🚨 Do NOT change any of the code below 
year = int(input()) # Enter a year
month = int(input()) # Enter a month
days = days_in_month(year, month)
print(days)

