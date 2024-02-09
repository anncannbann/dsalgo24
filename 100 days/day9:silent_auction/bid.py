from replit import clear
#HINT: You can call clear() to clear the output in the console.


from art import logo


print(logo)

dict={}
noppl =True

def find_high(bidding):
  high =0
  for key in bidding:
    bids = bidding[key]
    if bids >high:
      high = bids
      winner = key

  print(winner)

while noppl:
  name = input("what is your name?") 
  bid = int(input("enter bid")) 
  dict[name]= bid
  x = input("are there any other bidders?")
  if x =='no':
    noppl=False
    find_high(dict)
  elif x =="yes":
    clear()

  else:
    print("invalid input")
  


    
