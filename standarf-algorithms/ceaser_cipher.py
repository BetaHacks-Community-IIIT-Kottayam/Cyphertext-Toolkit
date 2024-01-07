def ceaser_encrypt(s, k):
    s = s.upper()
    str_result = ""

    for char in s:
        n = ord(char)
        n -= 64
        n = ((n + k) % 26) # just a small change here
        n += 64
        str_result += chr(n)

    return str_result

def ceaser_decrypt(s, k):
    return ceaser_encrypt(s, -k)


s = input("Enter string: ")
k = int(input("Enter the key/shift value: "))

encipher = ceaser_encrypt(s, k)
decipher = ceaser_decrypt(encipher, k)

print("Encrypted", encipher)
print("Decrypted", decipher)