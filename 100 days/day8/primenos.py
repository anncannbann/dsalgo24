# Write your code below this line 👇

def prime_checker(n):
    is_prime = True

    if n %2 ==0:
        is_prime = False
    else:
        for num in range(3,int((n+1)/2)):
            if n %num ==0:
                #print(n,num)
                is_prime = False
                

    if is_prime:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")




# Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input()) # Check this number
prime_checker(n)