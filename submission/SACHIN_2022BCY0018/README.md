# Rail Fence Cipher Encryption and Decryption

This Python code provides functions for encrypting and decrypting text using the Rail Fence Cipher, also known as the zigzag cipher.

## Features

- Encryption of plaintext to ciphertext using a provided key.
- Decryption of ciphertext back to plaintext using the same key.

## Usage

1. **Encryption**:
   - The `encryption(plain_text, key)` function encrypts the given `plain_text` using the provided `key`.
   - Returns the encrypted ciphertext.

   **Example**:
   - plain_text = ATTACK AT ONCE
   - key = 2
     
***Writing the Message***:
 - Write the plaintext message diagonally on the rails of the fence from top to bottom, moving up        and down like a zigzag pattern.
 - Each character of the plaintext is written on a different rail. The first character goes on the first rail, the second character on the second rail, and so on.
 - When you reach the bottom rail, reverse the direction and start moving up the fence.
   
***Reading***:
- Once the entire message is written on the rails, read off the characters row by row, starting from    the top rail row-wise.
- Encrypted_text: ATC TOCTAKA NE

2. **Decryption**:
   - The `decryption (encrypted_text, key)` function decrypts the given `encrypted_text` using the provided `key`.
   - Returns the plain text.
     
   **Example**:
   - Encrypted_text  =  ATC TOCTAKA NE
   - key = 2
    
***Writing the Message***:
- Write the encrypted message row-wise on the rails.
  
***Reading***:
- Once the entire message is written on the rails, read off the characters in diagonal (zig-zag) method, starting from the top rail.
- Decrypted_text: ATTACK AT ONCE



