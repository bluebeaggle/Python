


alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(text_temp, shift_temp) :
    result = ''
    for letter in text_temp :
        position = alphabet.index(letter) + shift_temp
        if position > 26 :
            position -= 26
            result += alphabet[position]
        else : 
            result += alphabet[position]
    print(result)

def decode(text_temp, shift_temp) :
    result = ''
    for letter in text_temp :
        position = alphabet.index(letter) - shift_temp
        if position < 0 :
            position += 26
            result += alphabet[position]
        else :
            result += alphabet[position]
    print(result)
            
encrypt(text, shift)
decode(text, shift)