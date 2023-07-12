alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(plain_text,shift_count):
    
    cipher_text=""
    for letter in plain_text:
        position=alphabet.index(letter)
        new_position=position + shift_count
        new_letter=alphabet[new_position]
        cipher_text += new_letter
    print(f"The encode text is {cipher_text}")

#Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.
def decrypt(cipher_text,shift_count):
    plain_text=""
    for letter in cipher_text:
        position=alphabet.index(letter)
        new_position=position-shift_count
        new_letter=alphabet[new_position]
        plain_text += new_letter
    print(f"The decode text is {plain_text}")
 

if direction == 'encode':
    encrypt(plain_text=text,shift_count=shift)
else:
    decrypt(cipher_text=text,shift_count=shift)
