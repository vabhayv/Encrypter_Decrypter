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


wanna_try_again = True

while wanna_try_again:
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
            else :
                print("\n***PLEASE SELECT THE CORRECT OPERATION***\n")
            shifted_text += availabe_symbols[new_position]
        print(f"The {choosen_direction}d text is: \n{shifted_text} \n  ")
    
    shift = shift%62
    
    encrypt_decrypt(user_text=text, shift_no=shift,choosen_direction=direction)  
    
    user_choice = input("Wanna try again?\nyes or no (default is no) : ")
    if user_choice == "yes" :
        wanna_try_again = True
        print("Here....\n")
    elif user_choice == "no" :
        wanna_try_again = False
        print("I hope you enjoyed it, visit again :)")
    else:
        wanna_try_again = False
        print("I hope you enjoyed it :)")







