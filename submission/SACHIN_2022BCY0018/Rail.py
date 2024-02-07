 #Encreption code
def encryption(plain_text, key):
    cipher_text = ""
    key_repeated = (key * (len(plain_text) // len(key) + 1))[:len(plain_text)]
    for i in range(len(plain_text)):
        if plain_text[i].isalpha():
            C = (ord(plain_text[i]) + ord(key_repeated[i])) % 26
            cipher_text += chr(C + ord('A'))
        else:
            cipher_text += plain_text[i]
    return cipher_text


#Decryption Code
def decryption(encrypted_text, key):
    plain_text = ""
    key_repeated = (key * (len(encrypted_text) // len(key) + 1))[:len(encrypted_text)]
    for i in range(len(encrypted_text)):
        if encrypted_text[i].isalpha():
            P = (ord(encrypted_text[i]) - ord(key_repeated[i])) % 26
            plain_text += chr(P + ord('A'))
        else:
            plain_text += encrypted_text[i]
    return plain_text

plain_text = input("Enter the plain text: ")
key = input("Enter the key: ")
encrypted_text = encryption(plain_text, key)
print("The encrypted message is:", encrypted_text)
decrypted_message = decryption(encrypted_text, key)
print("The decrypted message is:", decrypted_message)
