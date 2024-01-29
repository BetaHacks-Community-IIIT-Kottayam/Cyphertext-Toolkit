import string

def prepare_text(text, key):
    text = text.upper().replace("J", "I")
    key = key.upper().replace("J", "I")
    return text, key

def create_key_square(key):
    key_square = list(key)
    alphabet = string.ascii_uppercase.replace("J", "")
    for char in alphabet:
        if char not in key_square:
            key_square.append(char)
    key_square = [key_square[i:i+5] for i in range(0, 25, 5)]
    return key_square
def encrypt_digraph(digraph, key_square):
    row1, col1 = find_indices(digraph[0], key_square)
    row2, col2 = find_indices(digraph[1], key_square)
    if row1 == row2:
        col1 = (col1 + 1) % 5
        col2 = (col2 + 1) % 5
    elif col1 == col2:
        row1 = (row1 + 1) % 5
        row2 = (row2 + 1) % 5
    else:
        col1, col2 = col2, col1
    return key_square[row1][col1] + key_square[row2][col2]

def find_indices(char, key_square):
    for i in range(5):
        for j in range(5):
            if key_square[i][j] == char:
                return i, j

def encrypt(text, key):
    text, key = prepare_text(text, key)
    key_square = create_key_square(key)
    cipher_text = ""
    for i in range(0, len(text), 2):
        digraph = text[i:i+2]
        if len(digraph) == 1:
            digraph += "X"  
        cipher_text += encrypt_digraph(digraph, key_square)
    return cipher_text

key = str(input("enter the key : ")) 
plain_text = str(input(" enter the plain_text: ")) 
cipher_text = encrypt(plain_text, key)
print(cipher_text)  