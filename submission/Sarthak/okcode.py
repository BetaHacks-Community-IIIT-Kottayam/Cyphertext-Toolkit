# Define a dictionary mapping each English letter to its Morse code equivalent
morse_code_dict = {'A': '.-', 'B': '-...',
                  'C': '-.-.', 'D': '-..', 'E': '.',
                  'F': '..-.', 'G': '--.', 'H': '....',
                  'I': '..', 'J': '.---', 'K': '-.-',
                  'L': '.-..', 'M': '--', 'N': '-.',
                  'O': '---', 'P': '.--.', 'Q': '--.-',
                  'R': '.-.', 'S': '...', 'T': '-',
                  'U': '..-', 'V': '...-', 'W': '.--',
                  'X': '-..-', 'Y': '-.--', 'Z': '--..',
                  '1': '.----', '2': '..---', '3': '...--',
                  '4': '....-', '5': '.....', '6': '-....',
                  '7': '--...', '8': '---..', '9': '----.',
                  '0': '-----', ' ': '/'}

def ok_code_encode(text):
    # Convert each character to custom code and join them with a space
    custom_code_list = [morse_code_dict[letter.upper()].replace('.', 'o').replace('-', 'k') for letter in text]
    custom_code_string = ' '.join(custom_code_list)
    return custom_code_string


# Define a dictionary mapping each Morse code equivalent to its English letter
reverse_morse_code_dict = {'.-': 'A', '-...': 'B',
                           '-.-.': 'C', '-..': 'D', '.': 'E',
                           '..-.': 'F', '--.': 'G', '....': 'H',
                           '..': 'I', '.---': 'J', '-.-': 'K',
                           '.-..': 'L', '--': 'M', '-.': 'N',
                           '---': 'O', '.--.': 'P', '--.-': 'Q',
                           '.-.': 'R', '...': 'S', '-': 'T',
                           '..-': 'U', '...-': 'V', '.--': 'W',
                           '-..-': 'X', '-.--': 'Y', '--..': 'Z',
                           '.----': '1', '..---': '2', '...--': '3',
                           '....-': '4', '.....': '5', '-....': '6',
                           '--...': '7', '---..': '8', '----.': '9',
                           '-----': '0', '/': ' '}

def ok_code_decode(custom_code):
    # Split the custom code into individual codes and convert each back to English letter
    text_list = [reverse_morse_code_dict[code.replace('o', '.').replace('k', '-')] for code in custom_code.split()]
    text_string = ''.join(text_list)
    return text_string
