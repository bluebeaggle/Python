total_bill = float(input("What was the total bill? $"))
tip_percent = int(input("What percentage tip would you line to give? 10,12, or 15? ")) / 100
people = int(input("How many people to splite the bill? "))

pay = (total_bill *(1+tip_percent)) / people
pay = round(pay, 2)

print(f"Each person should pay: ${pay}")