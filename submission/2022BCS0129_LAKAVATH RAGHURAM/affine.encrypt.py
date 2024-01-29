def encrypt(plaintext, k1, k2):
    ciphertext = ""
    n = 26
    for char in plaintext:
        if char.isalpha(): 
            if char.islower():
                char_index = ord(char) - ord('a')
                encrypted_index = (k1 * char_index + k2) % n
                encrypted_char = chr(encrypted_index + ord('a'))
            elif char.isupper():
                char_index = ord(char) - ord('A')
                encrypted_index = (k1 * char_index + k2) % n
                encrypted_char = chr(encrypted_index + ord('A'))
        else:
            encrypted_char = char
        ciphertext += encrypted_char
    return ciphertext
if _name_ == "_main_":
    plaintext = str(input("enter the plain text: "))
    k1 = int(input("enter the k1 key : "))
    k2 = int(input("enter the k2 key : "))
    ciphertext = encrypt(plaintext, k1, k2)
    print("Encrypted:", ciphertext)