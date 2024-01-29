def encrypt(text, key):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            char = char.upper()
            char_index = ord(char) - ord('A')
            encrypted_index = (char_index * key) % 26
            encrypted_char = chr(encrypted_index + ord('A'))
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text
if __name__ == "__main__":
    plaintext = str(input("enter the palin_text : ")) 
    key = int(input("enter the key : "))
    ciphertext = encrypt(plaintext, key)
    print("Encrypted:", ciphertext)
