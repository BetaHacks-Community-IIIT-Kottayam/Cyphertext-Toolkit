from nltk.tokenize import word_tokenize
from nltk.corpus import words
"""
1. Please execute run_me.py before executing the code so that it install all the requirements and only for IIIT-K studnets please use VPN as run_me.py download some data which require vpn

2. This program encode a given text using pig latin and while encryption it ignore all the wors with length less than or equal to 3

3. This has a restriction it can only decrypt words which are a part of english dictionary so please do not use slangs 
"""

# these are some funciton that will be used in encrypt and decrypt functions
def encrypt_word(text): # this function encrypt a single word
    vowel=["a","e","i","o","u"]
    text=text.lower()
    if len(text)<=3:
        return text
    elif text[0] in vowel:
        return text+"yay"
    else:
        encrypted_text=text
        for i in text:
            if i in vowel:
                return encrypted_text+"ay"
            encrypted_text= encrypted_text[1:]+encrypted_text[0]
        return encrypted_text+"ay" 
    
def decrypt_word(word):
    if len(word)<=3:
        return word
    elif word[len(word)-3::] == "yay":
        return word[:-3:]
    else:
        word=word[:-2:]
        while (word not in words.words()):
            word=word[-1]+word[:-1:]
        return word



#this is our main encryption program other funcitons are for supporting it
def encrypt(text): #this encrypts complete sentece usign encrypt word function
    words_list=word_tokenize(text)
    encrypted_text=""
    for i in words_list:
        encrypted_text += encrypt_word(i) + " "
    return encrypted_text

#this is decryption program for pig latin using decrypt word funciton
def decrypt(text):
    text=text.lower()
    words_list=word_tokenize(text)
    decrypted_text=""
    for i in words_list:
        decrypted_text+=decrypt(i) + " "
    return decrypted_text