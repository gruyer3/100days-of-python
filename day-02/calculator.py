print(f"Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = float(input("How much tip would you like to give? 10, 12, or 15? "))
people = float(input("How many people to split the bill? "))

total_bill = bill * (tip / 100) + bill
bill_per_one = total_bill / people

print(f"Each person should pay: ${round(bill_per_one, 2)}")