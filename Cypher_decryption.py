def custom_decipher(encrypted_text):
    decrypted_text = ""
    for i, char in enumerate(encrypted_text):
        if char.isalpha():
            if i % 2 == 0:
                decrypted_text += chr((ord(char) - 5 - ord('A')) % 26 + ord('A'))
            else:
                symbols = "!@#$%^&*()_+-=[]{}|;':,.<>?/"
                decrypted_text += symbols[ord(char) - ord('A')]
        else:
            symbols = "!@#$%^&*()_+-=[]{}|;':,.<>?/"
            decrypted_text += chr(ord('A') + symbols.index(char))
    return decrypted_text
def main():
    encrypted_text = input("Enter the text to decrypt: ").upper()
    decrypted_text = custom_decipher(encrypted_text)
    print("Decrypted text:", decrypted_text)
if __name__ == "__main__":
    main()
