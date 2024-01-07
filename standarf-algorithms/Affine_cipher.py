def affine_encrypt(s, a, b):
    str_result = ""
    s = s.upper()
    for char in s:
        n = ord(char)
        n -= 64
        n = ((n * a) + b) % 26
        n += 64
        str_result += chr(n)

    return str_result

def affine_decrypt(s, a, b):
    s = s.upper()
    str_result = ""
    for char in s:
        n = ord(char)
        n -= 64  # Assuming uppercase letters
        # Calculate the inverse of the key modulo the alphabet size
        key_inverse = pow(a, -1, alphabet_size)
        n = ((n-b) * key_inverse) % alphabet_size
        n += 64  # Assuming uppercase letters
        str_result += chr(n)
        
    return str_result

s = input("Enter the message: ")
a = int(input("Enter a value: "))
b = int(input("Enter b value: "))
alphabet_size = 26  # Assuming a standard English alphabet

encipher = affine_encrypt(s,a,b)
decipher = affine_decrypt(encipher, a, b)

print("Encrypted", encipher)
print("Decrypted", decipher)