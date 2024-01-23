def custom_decipher(encrypted_text):
    shift_start = int(encrypted_text[0])
    shift_end = int(encrypted_text[-1]) 
    shift = shift_end * 10 + shift_start
    decrypted_text = ""
    for i, char in enumerate(encrypted_text[1:-1]):
        if char.isalpha():
            if i % 2 == 0:  # even position
                decrypted_text += chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            else:
                symbols = "!@#$%^&*()_+-=[]{}|;':,.<>?/"
                decrypted_text += symbols[ord(char) - ord('A')]
        elif char.isspace():  # handle spaces
            decrypted_text += ' '
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
