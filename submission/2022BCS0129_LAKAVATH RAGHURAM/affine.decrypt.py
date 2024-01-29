def mod_inverse(a, m):
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return None
def decrypt(ciphertext, k1, k2):
    plaintext = ""
    n = 26
    k1_inv = mod_inverse(k1, n)
    if k1_inv is None:
        print("Error: The key k1 does not have an inverse.")
        return ""
    for char in ciphertext:
        if char.isalpha():
            if char.islower():
                char_index = ord(char) - ord('a')
                decrypted_index = (k1_inv * (char_index - k2)) % n
                decrypted_char = chr(decrypted_index + ord('a'))
            elif char.isupper():
                char_index = ord(char) - ord('A')
                decrypted_index = (k1_inv * (char_index - k2)) % n
                decrypted_char = chr(decrypted_index + ord('A'))
        else:
            decrypted_char = char
        plaintext += decrypted_char
    return plaintext

if _name_ == "_main_":
    ciphertext = str(input("enter the cipher text: "))
    k1 = int(input("enter the k1 key: "))
    k2 = int(input("enter the k2 key: "))
    plaintext = decrypt(ciphertext, k1, k2)
    print("Decrypted:", plaintext)