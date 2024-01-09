from nltk.corpus import words
from nltk.tokenize import word_tokenize

def check_word(word):
    return(word.lower() in words.words())
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def are_coprime(num1, num2):
    return gcd(num1, num2) == 1
def check_all_words(sent):
    words_list=word_tokenize(sent)
    for i in words_list:
        if i not in words.words():
            return False
    return True

s=input("Enter Encrypted text:- ")
s=s.upper()
possibilities=[]
for multiplicative_key in range(1,26):
    if are_coprime(26,multiplicative_key):
        for addition_key in range(26):
            e=""
            for i in s:
                if i==" ":
                    e+=' '
                    continue
                temp=ord(i)-64
                temp=pow(multiplicative_key,-1,26)*(temp-addition_key)
                temp=temp%26
                temp+=64
                e+=chr(temp)
            possibilities.append(e)
            if check_word(word_tokenize(e)[0]) and "@" not in e :
                if check_all_words(e.lower()):
                    print("Decrypted text is ",e)
                    print("And the addition key is : ",addition_key)
                    print("And the multiplication key is : ",multiplicative_key)
choise =input("If you want to see all possibilities enter Y else press enter:- ")
if choise.lower()=='y':
    for i in range(len(possibilities)):
        print(i,". ",possibilities[i])