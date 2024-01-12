

# import random
# import string
# import sys

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

def roman_to_int(s):
    prev_value = 0
    result = 0
    for letter in s:
        curr_value = new_roman_dict[letter]
        if curr_value > prev_value:
            result += curr_value - 2 * prev_value
        else:
            result += curr_value
        prev_value = curr_value
    return result





def decrypt(sentence):
    sentence = simple_swap(sentence)
    decrypted_combined_roman = ""
    decrypted_roman = ""
    answer = ""
    for character in sentence:
        if character in new_roman_dict or character == 's':
            if character == 's':
             decrypted_combined_roman = decrypted_combined_roman + ' '
            else:
             decrypted_combined_roman = decrypted_combined_roman + character
    for character in decrypted_combined_roman:
        if character == ' ':
            integer_obtained =  roman_to_int(decrypted_roman)
            key_to_find = ''
            for key,value in alphabet_dict.items():
                if value == integer_obtained:
                    key_to_find = key
            answer = answer + key_to_find
            decrypted_roman = ""

        else:
            decrypted_roman = decrypted_roman + character
    return answer


#complete thing now


data = input("enter the data you wish to be decrypted")
print("The decryptred data is " + decrypt(data))

