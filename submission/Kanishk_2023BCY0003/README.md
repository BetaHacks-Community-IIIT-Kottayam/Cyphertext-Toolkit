# 🚀 About Me
I am Kanishk Mittal, a student at the Indian Institute of Information Technology Kottayam.

# About the Folder

This folder contains the following Python programs:

- `affine_cipher_brute_force_decoder.py`
- `Pig_latin_combined.py`
- `Cisco_encryption.py`
- `runme.py` 

## Python Library Installation Script

Simplifies the installation process for external libraries required for a specific Python project using `pip`. Also ensures NLTK data is downloaded.

### Note

- Ensure Python and `pip` are installed.
- Administrative privileges might be needed depending on your Python environment.

## affine_cipher_brute_force_decoder.py

### Overview

Decrypts text encrypted using the Affine cipher. Systematically explores possible decryption options using multiplicative and additive keys, checking for valid English words.

### How to Use

1. **Input Encrypted Text**: Enter the encrypted text when prompted.
2. **Analysis and Decryption**: Explores possible decryption options and displays results if found.
3. **View All Possibilities (Optional)**: Choose to view all attempted decryption possibilities. 

### Decryption Formula
- `D(x) = a^(-1)(x - b) mod m`

### Note

- Assumes the input is encrypted using the Affine cipher with a single-word key.
- May not be accurate for short or highly encrypted texts.
- NLTK's words corpus is used for valid English words.

## Pig_latin_combined.py

### Overview

Encodes and decodes text using the Pig Latin language. Ignores words with length <= 3 during encryption and has limitations in decrypting non-dictionary words.

### How to Use

1. **Encryption**: Use `encrypt(text)` for Pig Latin encoding.
2. **Decryption**: Utilize `decrypt(text)` for decoding Pig Latin sentences.

### Encryption and Decryption Formulas

- **Encryption**: 
  - If the word starts with a vowel (A, E, I, O, U), add `-yay` at the end.
  - If the word begins with consonants, move them to the end and add `-ay`.
- **Decryption**: 
  - Inverse translation involves removing the suffix `-AY` and possibly repositioning consonants at the beginning. Verify each possibility using `NLTK`.

### Note

- Uses NLTK's `words.words()` for English dictionary checking.
- Slang and non-dictionary words may not decrypt accurately.

## Cisco-Encrypter

### Overview

A self-made encrypter that replaces spaces, certain characters, and performs unique character substitutions.

### How to Use

1. **Encryption**: Use `encrypt(text)` for Cisco's custom algorithm.
2. **Decryption**: Utilize `decrypt(text)` for decoding text encrypted with Cisco's algorithm.

### Encryption and Decryption Formulas

- **Encryption**: Replaces spaces with `$$` and replaces each character with two whose sum of ASCII values is the same as the original character.
- **Decryption**: Access characters in pairs, replacing `$$` with a space and each pair with a character whose ASCII value is the sum of both characters.
