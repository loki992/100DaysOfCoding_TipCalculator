print("Welcome to the tip calculator!")
total_bill = round(int(input("What was the total bill? $ ")), 2)
tip_percentage = float(input("How much % tip would you like to give? 10, 12 or 15? "))
people_quant = int(input("How many people to split the bill? "))
total_with_tip = total_bill/(100/tip_percentage)+total_bill
payment_per_person = round(total_with_tip/people_quant, 2)
print(f"Each person should pay: ${payment_per_person}")