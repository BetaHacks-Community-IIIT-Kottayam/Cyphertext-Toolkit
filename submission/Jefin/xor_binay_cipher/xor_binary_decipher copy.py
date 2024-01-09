cipher_text = input("Enter your ciphered text: ")
key = input("Enter your Binary key: ")
try:
    key_list = list(key)
    key_list = [int(x) for x in key_list]

    cipher_text_length = len(cipher_text)
    key_length = len(key_list)

    if (cipher_text_length > key_length):
        r = cipher_text_length // key_length + 1
        key_list *= r

    decipher_text = []

    for i in range(cipher_text_length):
        if key_list[i] == int(cipher_text[i]):
            decipher_text.append('0')
        else:
            decipher_text.append('1')

    deciphered_text = ''.join(decipher_text)

    original_string = ""
    for i in range(0, len(deciphered_text), 8):
        binar = deciphered_text[i:i+8]
        decimal_value = int(binar, 2)
        original_string += chr(decimal_value)

    print("The deciphered text is:", original_string)
except:
    print("error occured")
    
