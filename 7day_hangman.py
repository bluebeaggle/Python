import random
word_list=["ardvark", "baboon", "camel"]

# game_start = random.choice(word_list)
# hangman=[]
# for i in game_start :
#     hangman.append(i)
# question = []
# for i in range(len(hangman)) :
#     question.append("- ")

# print(hangman)
# print(question)

# life = 5

# while(True) :
#     customer_input=input("Guess ? \n")
#     if customer_input in hangman :
#         for i in range(len(hangman)) :
#             if customer_input is hangman[i] :
#                 question[i] = customer_input
#     else :
#         life -=1
#         if life == 0:
#             print(f"Your life is {life}")
#             print("You lose")
#             break
#     if "- " not in question :
#         print(question)
#         print("Success!")
#         break
#     print(life)
#     print(question)
    
    
    
    
chosen_word = random.choice(word_list)
display = []
for letter in chosen_word :
    display += '_'

print(display)



def question() :
    guess = input("Geuss a letter : ").lower()
    for i in range(len(chosen_word)) :
        letter = chosen_word[i]
        if letter == guess :
            display[i] = letter
    print(display)

while(True) :
    if '_' in display :
        question()
    else :
        print("You win!")
        break


