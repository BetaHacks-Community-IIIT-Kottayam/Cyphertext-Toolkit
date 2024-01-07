def multiplicative_cipher_encrypt(s, k):
    s = s.upper()
    str_result = ""
    for char in s:
        a = ord(char)
        a -= 65
        a = (a * k) % 26
        a += 65
        str_result += chr(a)

    return str_result

def multiplicative_cipher_decrypt(s, key):
    key_inverse = pow(key, -1, alphabet_size)

    return multiplicative_cipher_encrypt(s, key_inverse)

# Input
s = input("Enter the string: ")
key = int(input("Enter the key: "))
alphabet_size = 26  # Assuming a standard English alphabet

encipher = multiplicative_cipher_encrypt(s, key)
decipher = multiplicative_cipher_decrypt(encipher, key)

print("Encrypted: ", encipher)
print("Decrypted: ", decipher)