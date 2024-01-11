string = input("Enter your string: ")
key = input("Enter your Binary key: ")
try:
    key_list = list(key)
    key_list = [int(x) for x in key_list]
    binary_string = []

    for i in range(0, len(string)):
        alphabet = string[i]
        alphabet = ord(alphabet)
        binary_alphabet = bin(alphabet)[2:].zfill(8)  
        binary_string += list(binary_alphabet)

    binary_length = len(binary_string)
    key_length = len(key_list)

    if binary_length > key_length:
        r= binary_length // key_length + 1
        key_list *= r

    cipher_text = []

    for i in range(binary_length):
        if key_list[i] == int(binary_string[i]):
            cipher_text.append('0')
        else:
            cipher_text.append('1')

    cipher_text = ''.join(cipher_text)
    print("The ciphered text is:", cipher_text)
except:
    print("error occured")