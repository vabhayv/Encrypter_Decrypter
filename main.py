alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

wanna_try_again = True
while wanna_try_again:
    direction = input("Type 'encode' to Encrypt and Type 'decode' to Decrypt: \n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift code:\n"))
       
    def encrypt_decrypt(plain_text, shift_amount):
        user_text = ""
        for letter in plain_text:
            position = alphabet.index(letter)
            if direction == 'encode':
                new_position = position + shift_amount
            elif direction == 'decode':
                new_position = position - shift_amount
            new_letter = alphabet[new_position]
            user_text += new_letter
        if direction == 'encode':
            print(f"The encoded text is {user_text}")
        elif direction == 'decode':
            print(f"The decoded text is {user_text}")
            
                
        
    
    encrypt_decrypt(plain_text=text, shift_amount=shift)
    say = input("wanna use again? type 'yes' to continue or 'no' to stop")
    if say == 'no':
        print("hope you enjoy it :)")
        wanna_try_again = False
    elif say == 'yes':
        print("here you go !!")
        wanna_try_again = True
    
    
    
    