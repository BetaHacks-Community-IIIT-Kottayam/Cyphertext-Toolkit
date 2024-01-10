

import random
import string
import sys

val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
roman_dict = {'A': 1, 'R': 5, 'U': 10, 's': 50, 'H': 100, 'M': 500, 'b': 1000}
syms = {}
new_roman_dict = {}
alphabet_dict = {}
special_characters = "!@#$%^&*()_-+=<>789?3456/12[]{}|"
number = input("enter ur passkey (three digit number not containing 0)")
for character in number:
    if character == '0':
        print("invalid input")
        print("invalid input")
        exit()
num = int(number)
first_num = (int(num/100))
second_num = int(num/10)%10
third_num = (num%10)
the_other_two= second_num
digits = [ first_num , second_num , third_num]
start = first_num ** 2
#note to make check of passkey later

def valueforalphabet(dict):
   l = 0
   for number in range(32,127):
     dict[chr(number)] = start + l
     l  = l + start

def simple_swap(tbj):
    tbj_list = list(tbj)
    length = len(tbj_list)
    m = 0
    while m < length - third_num:
        temp = tbj_list[m]
        tbj_list[m] = tbj_list[m+third_num]
        tbj_list[m+third_num] = temp
        m = m + 2 * third_num
    jumbled_string = ''.join(tbj_list)
    return jumbled_string

def update_dict(dict):
    for old_key in dict:
     new_roman_dict[chr(ord(old_key)+the_other_two)] = dict[old_key]
    return new_roman_dict

valueforalphabet(alphabet_dict)

new_roman_dict = update_dict(roman_dict)

key_list = list(new_roman_dict)
i = 0
j = 6
while i < 13:
    syms[i] = key_list[j]
    j = j - 1
    i = i +2
i = 1
j = 6
k = 4
while i < 10:
    syms[i] = key_list[k] + key_list[j]
    syms[i+2] = key_list[k] + key_list[j-1]
    i = i + 4
    k = k - 2
    j = j - 2


def int_to_roman(num):
    i = 0
    roman_num = ''
    while num > 0:
        for _ in range(num // val[i]):
            roman_num += syms[i]
            num -= val[i]
        i += 1
    return roman_num

def randomletters():
    gibberish = ""
    for number in range(0, random.randint(11, 15)):
        random_letter = random.choice(string.ascii_uppercase)
        random_special_character = random.choice(special_characters)
        while random_special_character in new_roman_dict:
            random_special_character = random.choice(special_characters)
        while random_letter in new_roman_dict:
            random_letter = random.choice(string.ascii_uppercase)
        if number%3 == 0:
         gibberish = gibberish + random_letter + random_special_character
    return gibberish


def encrypt(sentence):
    encrypted_data = ""
    for character in sentence:
        temp_int = alphabet_dict[character]
        temp_roman = int_to_roman(temp_int)
        encrypted_data = encrypted_data + randomletters()
        encrypted_data = encrypted_data + temp_roman + randomletters() + 's'
    encrypted_data = encrypted_data + randomletters()
    return simple_swap(encrypted_data)




#complete thing now


data = input("enter the data you want to be encrypted")
print("The Encrypted Data is " + encrypt(data))
