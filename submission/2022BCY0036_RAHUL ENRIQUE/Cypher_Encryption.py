import random
def custom_cipher(text):
    shift = random.randint(10, 99) 
    shift_start = shift % 10  
    shift_end = shift // 10  
    encrypted_text = str(shift_start)
    for i, char in enumerate(text):
        if char.isalpha():
            if i % 2 == 0:
                encrypted_text += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:  # odd position
                symbols = "!@#$%^&*()_+-=[]{}|;':,.<>?/"
                encrypted_text += symbols[ord(char) - ord('A')]
        elif char.isspace():
            encrypted_text += ' '
    encrypted_text += str(shift_end) 
    return encrypted_text
def main():
    plaintext = input("Enter the text to encrypt: ").upper()
    encrypted_text = custom_cipher(plaintext)
    print("Encrypted text:", encrypted_text)
if __name__ == "__main__":
    main()
