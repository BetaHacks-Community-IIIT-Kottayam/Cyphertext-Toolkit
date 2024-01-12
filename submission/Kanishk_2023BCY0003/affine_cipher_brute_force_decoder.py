from nltk.corpus import words
from nltk.tokenize import word_tokenize

def check_word(word, word_set):
    return word.lower() in word_set

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def are_coprime(num1, num2):
    return gcd(num1, num2) == 1

def check_all_words(sent, word_set):
    words_list = word_tokenize(sent)
    return all(word in word_set for word in words_list)

def decrypt_text(s, word_set):
    possibilities = []
    for multiplicative_key in range(1, 26):
        if are_coprime(26, multiplicative_key):
            inv_multiplicative_key = pow(multiplicative_key, -1, 26)
            for addition_key in range(26):
                e = ""
                for i in s:
                    if i == " ":
                        e += ' '
                        continue
                    temp = ord(i) - 64
                    temp = inv_multiplicative_key * (temp - addition_key) % 26
                    temp += 64
                    e += chr(temp)
                possibilities.append(e)
                if check_word(word_tokenize(e)[0], word_set) and "@" not in e:
                    if check_all_words(e.lower(), word_set):
                        print("Decrypted text is", e)
                        print("Addition key is:", addition_key)
                        print("Multiplication key is:", multiplicative_key)
    return possibilities

s = input("Enter Encrypted text: ").upper()
word_set = set(words.words())
possibilities = decrypt_text(s, word_set)

choice = input("If you want to see all possibilities, enter Y else press enter: ").lower()
if choice == 'y':
    for i, possibility in enumerate(possibilities):
        print(i, ". ", possibility)
