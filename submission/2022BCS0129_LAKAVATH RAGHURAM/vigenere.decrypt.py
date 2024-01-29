def vigenere_decrypt(ciphertext, key):
    plaintext = ''
    key_length = len(key)
    for i in range(len(ciphertext)):
        char = ciphertext[i]
        if char.isalpha():
            key_char = key[i % key_length].upper()
            shift = ord(key_char) - ord('A')
            if char.islower():
                plaintext += chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
            else:
                plaintext += chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
        else:
            plaintext += char
    return plaintext

ciphertext = str(input("enter the cipher text: "))
key = str(input("enter the key : "))
decrypted_text = vigenere_decrypt(ciphertext, key)
