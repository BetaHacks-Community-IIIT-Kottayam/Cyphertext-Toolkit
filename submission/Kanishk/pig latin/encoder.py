from nltk.tokenize import word_tokenize
def encrypt(text):
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
text=input("Enter the string which you want to encrypt:- ")
words_list=word_tokenize(text)
encrypted_text=""
for i in words_list:
    encrypted_text += encrypt(i) + " "
print("encrypted text: ",encrypted_text)