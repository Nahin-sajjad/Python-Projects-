print("Welcome to the tip calculator.")
bill=float(input("What was the total bill? $"))	

tip=int(input("What percentage tip would you like to give? 10, 12, or 15? "))

num_people=int(input("How many people to split the bill? "))

each_person=(bill/num_people)*(1+(tip/100))

print(f"Each person should pay: ${round(each_person,2)}")

