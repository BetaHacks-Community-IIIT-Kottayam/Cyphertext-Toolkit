def decrypt_text(encrypted_text, key):
    decrypted_text=[]
    encrypted_text=str(int(encrypted_text)//(key*key))
    decrypted_text=list(map(''.join, zip(*[iter(encrypted_text)]*3)))
    decrypted_text=[chr(int(x[::-1],8))  for x in decrypted_text ]
    return ''.join(decrypted_text)