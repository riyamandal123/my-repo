alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text,shift_count,cipher_direction):
    cipher_text=""
    for char in start_text:
        if char in alphabet:
            position=alphabet.index(char)
            if cipher_direction == "encode":
                new_position=position + shift_count
                new_letter = alphabet[new_position]
                cipher_text += new_letter
            elif cipher_direction == "decode":
                new_position=position - shift_count
                new_letter = alphabet[new_position]
                cipher_text += new_letter
        else:
            cipher_text += char
    print(f"The {cipher_direction} text is {cipher_text}")

while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26

    caesar(start_text=text,shift_count=shift,cipher_direction=direction)

    restart=input("Type 'yes' if you want to go again. Otherwise type 'no'.  ")
    if restart == 'yes':
        continue
    else:
        break
    





            
