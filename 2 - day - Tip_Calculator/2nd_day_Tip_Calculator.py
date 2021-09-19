print("Welcome to the tip calculator!")
total_bill = float(input("What was the total bill? $"))
per_tip = int(input("What percentage tip would you like to give? "))
friends = int(input("How many people to split the bill? "))

bill_plus_tip = total_bill + total_bill * per_tip/100

bill = bill_plus_tip/friends

print(f"Each person should pay: ${bill:.2f} ")