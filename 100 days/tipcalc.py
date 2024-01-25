print("Welcome to the tip calculator")

bill = float(input("Enter your bill"))

tipperc = int(input("What Percentage tip would you like to give 10,12,or 15"))

people = int(input("How many people to split the bill"))


pp = ((tipperc/100)*bill + bill)/ people   


#new thing to learn
finalpp = "{:.2f}".format(pp)

print(f"Each person should pay {finalpp}")
