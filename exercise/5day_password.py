# Go to: https://replit.com/@appbrewery/password-generator-start?v=1
#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
password = ''
for i in range(nr_letters) :
    password += letters[random.randrange(0,len(letters))]
for i in range(nr_symbols) :
    password += symbols[random.randrange(0,len(symbols))]
for i in range(nr_numbers) :
    password += numbers[random.randrange(0,len(numbers))]
print(password)
#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
password = ''
letter_count = 0
symbol_count = 0
number_count = 0
while(True) :
    if len(password) == nr_letters+nr_symbols+nr_numbers :
        break
    choice = random.choice([letters,numbers,symbols])
    if choice is letters :
        if letter_count >= nr_letters :
            continue
        else :
            password += random.choice(choice)
            letter_count += 1
    elif choice is numbers :
        if number_count >= nr_numbers :
            continue
        else :
            password += random.choice(choice)
            number_count += 1
    elif choice is symbols :
        if symbol_count >= nr_symbols :
            continue
        else :
            password += random.choice(choice)
            symbol_count +=1
print(password)


password_list= []
for i in range(nr_letters) :
    password_list.append(letters[random.randrange(0,len(letters))])
for i in range(nr_symbols) :
    password_list += symbols[random.randrange(0,len(symbols))]
for i in range(nr_numbers) :
    password_list += numbers[random.randrange(0,len(numbers))]
random.shuffle(password_list)
password = ''
for i in password_list :
    password += i
print(password)