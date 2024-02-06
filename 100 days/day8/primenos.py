# Write your code below this line 👇

def prime_checker(n):
  if n %2 ==0:
    print("It's not a prime number.")
  else:
    for num in range(3,int((n+1)/2)):
      if n %num ==0:
        #print(n,num)
        print("It's not a prime number.")
        break
      else:
        print("It's a prime number.")
        break


# Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input()) # Check this number
prime_checker(n)