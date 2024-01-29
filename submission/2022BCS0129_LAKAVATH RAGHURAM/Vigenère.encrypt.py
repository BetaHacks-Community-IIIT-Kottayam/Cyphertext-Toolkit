def vigenere_encrypt(plaintext, key):
    ciphertext = ''
    key_length = len(key)
    for i in range(len(plaintext)):
        char = plaintext[i]
        if char.isalpha():
            key_char = key[i % key_length].upper()
            shift = ord(key_char) - ord('A')
            if char.islower():
                ciphertext += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            else:
                ciphertext += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        else:
            ciphertext += char
    return ciphertext

plaintext = str(input("enter the plain text: "))
key = str(input("enter the key: "))
encrypted_text = vigenere_encrypt(plaintext, key)
print("Encrypted:", encrypted_text) 