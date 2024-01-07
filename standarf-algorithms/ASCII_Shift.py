def ascii_shift_encrypt(plaintext, shift):
    ciphertext = ""

    for char in plaintext:
        shifted_char = chr((ord(char) + shift) % 128)  # Assuming ASCII characters (0-127)
        ciphertext += shifted_char

    return ciphertext

def ascii_shift_decrypt(ciphertext, shift):
    return ascii_shift_encrypt(ciphertext, -shift)

# Example usage
plaintext = input("Enter the plaintext: ")
shift_value = int(input("Enter the shift value: "))

# Encryption
encrypted_text = ascii_shift_encrypt(plaintext, shift_value)
print("Encrypted text:", encrypted_text)

# Decryption
decrypted_text = ascii_shift_decrypt(encrypted_text, shift_value)
print("Decrypted text:", decrypted_text)
