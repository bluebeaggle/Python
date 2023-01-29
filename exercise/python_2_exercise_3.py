# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 1 year = 365 days, 52 weeks, 12 months
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
left_life = 90-int(age)
days = left_life * 365
weeks = left_life * 52
months = left_life * 12

print(f"You have {days} days, {weeks} weeks, and {months} months left.")