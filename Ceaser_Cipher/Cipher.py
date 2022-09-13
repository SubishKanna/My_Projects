from Cipher_DB import logo, alphabet

def caesar_cipher(text, shift, direction):
    text_index = []
    cipher_text = []
    for i in range(len(text)):
        text_index.append(alphabet.index(text[i]))
        
    if direction == "encode":
        for i in range(len(text_index)):
            if (text_index[i]+shift) >= len(alphabet):
                cipher_text.append(alphabet[(text_index[i]+shift)-(len(alphabet))])
            else:
                cipher_text.append(alphabet[text_index[i]+shift])
        
        print(f"\nThe encoded text is {cipher_text}")
        
    elif direction == "decode":
        for i in range(len(text_index)):
            cipher_text.append(alphabet[text_index[i]-shift])
        
        print(f"\nThe decoded text is {cipher_text}")
        

print(logo)
again = True
while again == True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift %=len(alphabet)
  
    caesar_cipher(text, shift, direction)
    yes_no = input("Type 'yes' if you want to continue. Otherwise type 'no.'")
    if yes_no == 'no':
        again = False
        print("Goodbye")        
        


