def custom_cipher(text):
    encrypted_text = ""
    for i, char in enumerate(text):
        if char.isalpha():
            if i % 2 == 0:  # even position
                encrypted_text += chr((ord(char) - ord('A') + 5) % 26 + ord('A'))
            else:  # odd position
                symbols = "!@#$%^&*()_+-=[]{}|;':,.<>?/"
                encrypted_text += symbols[ord(char) - ord('A')]
    return encrypted_text
def main():
    plaintext = input("Enter the text to encrypt: ").upper()
    encrypted_text = custom_cipher(plaintext)
    print("Encrypted text:", encrypted_text)
if __name__ == "__main__":
    main()
