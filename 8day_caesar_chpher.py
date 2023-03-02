alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
print(len(alphabet))
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(text_temp, shift_temp) :
    result = ''
    if shift_temp >= 26 :
        shift_temp %= 26
        print(shift_temp)
    for letter in text_temp :
        position = alphabet.index(letter) + shift_temp
        print(position)
        if position > 26 :
            position -= 26
            print(result, position)
        elif 
        else : 
            result += alphabet[position]
    print(f"The encode text is {result}")

def decrypt(text_temp, shift_temp) :
    result = ''
    if shift_temp >= 26 :
        shift_temp %= 26
    for letter in text_temp :
        position = alphabet.index(letter) - shift_temp
        if position < 0 :
            position += 26
            result += alphabet[position]
        else :
            result += alphabet[position]
    print(f"The decoded text is {result}")

if direction == "encode" :
    encrypt(text_temp=text, shift_temp=shift)
elif direction == "decode" :
    decrypt(text_temp=text, shift_temp=shift)
else : 
    print("Incorect")
    
def caesar(text_temp, shift_temp, direction_temp) :
    result = ''
    if shift_temp >= 26 :
        shift_temp %= 26
    if direction_temp == "encode" :
        for letter in text_temp :
            position = alphabet.index(letter) + shift_temp
            if position > 26 :
                position -= 26
                result += alphabet[position]
            else : 
                result += alphabet[position]
        print(f"The encode text is {result}")
    elif direction_temp == "decode" :
        for letter in text_temp :
            position = alphabet.index(letter) - shift_temp
            if position < 0 :
                position += 26
                result += alphabet[position]
            else :
                result += alphabet[position]
        print(f"The decod text is {result}")
        
caesar(text_temp=text, shift_temp=shift,direction_temp=direction)

def update_caesar(text_temp, shift_temp, direction_temp) :
    result = ''
    if shift_temp >= 26 :
        shift_temp %= 26
    if direction_temp == "decode" :
        shift_temp *= -1
    for letter in text_temp :
        position = alphabet.index(letter) + shift_temp
        if position > 26 :
            position -= 26
            result += alphabet[position]
        elif position < 0 : 
            position += 26
            result += alphabet[position]
        else :
            result += alphabet[position]
    print(f"The {direction_temp} text is {result}")

update_caesar(text_temp=text, shift_temp=shift,direction_temp=direction)

