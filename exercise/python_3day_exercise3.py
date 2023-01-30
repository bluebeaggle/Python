# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

score = 0
name3 = name1+name2
name3 = name3.lower()

for i in "true" :
    score += 10 * name3.count(i)

for i in "love" :
    score += name3.count(i)

if score <10 or score >90 :
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score >40 and score<50 :
    print(f"Your score is {score}, you are alright together.")
else :
    print(f"Your score is {score}")