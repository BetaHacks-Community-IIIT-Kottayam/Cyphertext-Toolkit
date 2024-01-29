1)additive Caesar Cipher Encryption/Decryption

This Python script implements the Caesar cipher encryption technique. The Caesar cipher is a substitution cipher where each letter in the plaintext is shifted a certain number of places down or up the alphabet.

Usage:
=>Clone the repository or download the additive.cipher.encrypt.py or additive.cipher.decrypt.py file.
=>Run the script using Python. Make sure you have Python installed on your system.
=>Enter the text you want to encrypt or decrypt when prompted.
=>Enter the shift value, which indicates the number of positions each letter in the plaintext/ciphertext should be shifted.
=>The script will output the encrypted/decrypted text.

Note
=>The script preserves the case of letters (uppercase or lowercase) in the original text.
=>Non-alphabetic characters (such as numbers, punctuation, and spaces) remain unchanged.


2)Affine Cipher Encryption and Decryption

This Python script implements the Affine cipher encryption and decryption techniques. The Affine cipher is a type of substitution cipher where each letter in the plaintext is mapped to its numeric equivalent, encrypted using a mathematical function, and then converted back to a letter.

Features
=>Encryption: Convert plaintext to ciphertext using the specified keys.
=>Decryption: Decrypt ciphertext back to plaintext using the inverse keys.

Notes
=>The keys k1 and k2 must satisfy certain conditions for the encryption and decryption processes to work correctly.
=>Ensure that the plaintext contains only alphabetical characters (A-Z, a-z) and no special characters or numbers.


3)Multiplicative Cipher Encryption and Decryption

This Python script implements the Multiplicative cipher encryption and decryption techniques. The Multiplicative cipher is a type of substitution cipher where each letter in the plaintext is multiplied by a key, modulo the alphabet size, to generate the ciphertext.

Features
=>Encryption: Convert plaintext to ciphertext using the specified key.
=>Decryption: Decrypt ciphertext back to plaintext using the inverse key.

Notes
=>The key must be chosen such that it has a modular multiplicative inverse in the alphabet size (26).
=>Ensure that the plaintext contains only alphabetical characters (A-Z, a-z) and no special characters or numbers.

4)Playfair Cipher Encryption

This Python script implements the Playfair cipher encryption technique. The Playfair cipher is a substitution cipher that uses a 5x5 grid of letters to encrypt pairs of letters in the plaintext.

Features
Encryption: Encrypts plaintext using the Playfair cipher algorithm.
Key Square: Generates the key square based on the given keyword.
Text Preparation: Prepares the plaintext and the key for encryption.

Notes
=>The key should contain only alphabetical characters (A-Z) and no special characters or numbers.
=>The plaintext can contain any characters, but they will be converted to uppercase.
=>The script automatically handles the replacement of "J" with "I" in the plaintext and the key.

5)Vigenère Cipher Encryption and Decryption

This Python script implements the Vigenère cipher encryption and decryption technique. The Vigenère cipher is a polyalphabetic substitution cipher that uses a keyword to encrypt and decrypt messages.

Features
=>Encryption: Encrypts plaintext using the Vigenère cipher algorithm.
=>Decryption: Decrypts ciphertext using the Vigenère cipher algorithm.
=>Key Handling: Handles the keyword for encryption and decryption.
=>Alphabet Handling: Supports uppercase and lowercase alphabets

Notes
=>The keyword should contain only alphabetical characters (A-Z, a-z) and no special characters or numbers.
=>Both the plaintext and the ciphertext can contain any characters, but they will be converted to uppercase.
=>The script automatically handles the wrapping of the keyword for encryption and decryption.