def decrypt(ciphertext, key):
    decrypted_text = ""
    alphabet_size = 26
    for i in range(alphabet_size):
        if (key * i) % alphabet_size == 1:
            multiplicative_inverse = i
            break
    else:
        return "Error: No modular multiplicative inverse for the given key."
    for char in ciphertext:
        if char.isalpha():
            char = char.upper()
            char_index = ord(char) - ord('A')
            decrypted_index = (char_index * multiplicative_inverse) % alphabet_size
            decrypted_char = chr(decrypted_index + ord('A'))
            decrypted_text += decrypted_char
        else:
            decrypted_text += char
    return decrypted_text
if __name__ == "__main__":
    ciphertext =str(input("enter the cipher text : "))
    key = int(input("enter the key : "))
    plaintext = decrypt(ciphertext, key)
    print("Decrypted:", plaintext)
