"""
Cisco-encrypter

!!! This is not a standard encrypter and is self made !!!

How it works:
    1. It replace a space it replace it by $$ 
    2. It replace the character "A" with "#A"
    3. It replace a single character with two character whose sum is same as the orignal character
        Example:- B is replaced by AA 
        Example:- C is replaced by AB 
        Example:- D is replaced by BB 
        Example:- E is replaced by BC and so on  
"""

def encrypt(text): # function to encrypt text
    text=text.upper() 
    encrypted_text=""
    for i in text:
        temp=ord(i)-64
        if i ==" ":
            encrypted_text+="$$"
        elif i== "A":
            encrypted_text+="#A"
        elif temp%2==0:
            encrypted_text+=chr(int(temp/2)+64)*2
        else:
            encrypted_text+=chr(int(temp/2)+64)+chr(int(temp/2)+65)
    return encrypted_text

def decrypt(text): #funciotn to decrypt text
    text=text.upper()
    decrypted_text=""
    for i in range(0,len(text),2):
        if((text[i]+text[i+1])=="$$"):
            decrypted_text+=" "
        elif((text[i]+text[i+1])=="#A"):
            decrypted_text+="A"
        else:
            decrypted_text+=chr(((ord(text[i])-64)+(ord(text[i+1])-64))+64)
    return decrypted_text