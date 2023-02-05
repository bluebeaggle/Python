# Banker Roulette

#Import the random module here

#Split string method
names_string = input("Give me everybody's names, separated by a comma.")
names = names_string.split(",")
#Don't change the code above

#Write your code below this line

import random
names_number = len(names)
random_name = random.randint(0,names_number-1)

print(f"{names[random_name]} is going to buy the meal today!")

person = random.choice(names)
print(person + " is going to buy the meal today!")

