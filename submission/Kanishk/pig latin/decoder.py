from nltk.tokenize import word_tokenize
from nltk.corpus import words

def decrypt(word):
    if len(word)<=3:
        return word
    elif word[len(word)-3::] == "yay":
        return word[:-3:]
    else:
        word=word[:-2:]
        while (word not in words.words()):
            word=word[-1]+word[:-1:]
        return word

text=input("Enter encrypted text:- ")
text=text.lower()
words_list=word_tokenize(text)
decrypted_text=""
for i in words_list:
    decrypted_text+=decrypt(i) + " "
print("Decrypted text is :- ",decrypted_text)