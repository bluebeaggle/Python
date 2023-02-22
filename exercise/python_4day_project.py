rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

competition = [rock, paper,scissors]
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
computer_choice = random.randint(0,2)

print(competition[user_choice])
print("Computer chose:")
print(competition[computer_choice])
if computer_choice == 0 :
    if user_choice==1:
        print("You win")
    elif user_choice==2:
        print("You lose")
    else :
        print("You tie")
elif computer_choice == 1:
    if user_choice==1:
        print("You tie")
    elif user_choice==2:
        print("You win")
    else :
        print("You lose")
else :
    if user_choice==1:
        print("You lose")
    elif user_choice==2:
        print("You tie")
    else :
        print("You win") 