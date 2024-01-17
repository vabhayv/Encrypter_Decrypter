availabe_symbols = [' ', '!', '@', '#', '$', '%', '&', '*', '(', ')', '_',
'+', '-', '/', '?', '.', ':', ';', '[', ']', '{', '}', '|', ',', '`', '~',
'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f',
'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 
'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', ' ', '!',
'@', '#', '$', '%', '&', '*', '(', ')', '_', '+', '-', '/', '?', '.', ':', ';', 
'[', ']', '{', '}', '|', ',', '`', '~', '0', '1', '2', '3', '4', '5', '6', '7', 
'8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 
'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 
'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 
'U', 'V', 'W', 'X', 'Y', 'Z' ]

direction = input("Type 'encode' to Encrypt or Type 'decode' to Decrypt: \n")
text = input("Type your message: \n")
shift = int(input("Type your code number: \n"))

def encrypt_decrypt(user_text,shift_no,choosen_direction):
    shifted_text = ""
    for letter in user_text:
        position = availabe_symbols.index(letter)
        if choosen_direction == "encode":
            new_position = position + shift_no
        elif choosen_direction == "decode":
            new_position = position - shift_no
        shifted_text += availabe_symbols[new_position]
    print(f"The {choosen_direction}d text is {shifted_text}")
    
    
def decrypt(decoded_text,shift_no):
    normal_text = ""
    for letter in decoded_text:
        position = availabe_symbols.index(letter)
        new_position = position - shift_no
        normal_text += availabe_symbols[new_position]
    print(f"The normal text is {normal_text}")


encrypt_decrypt(user_text=text, shift_no=shift,choosen_direction=direction)  
    







