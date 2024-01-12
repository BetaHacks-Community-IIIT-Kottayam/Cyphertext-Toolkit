## Random Evo Key Cipher
This cipher encrypts the text using a pregenerated key. If the character is at an odd index and the digit at the index modulo length of the key is also odd, then we increase the ASCII value of the character by the digit specified at the key, otherwise we decrement the specified digit. To decrypt the text, we implement the reverse using the same key given.

<i> By Allen Rai George </i>