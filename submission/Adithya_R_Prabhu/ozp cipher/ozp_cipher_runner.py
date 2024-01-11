import  ozp_cipher_decoder 
import ozp_cipher_encoder 
try:
    desc=input("do you want to Encrypt/Decrypt (e/d):-")


    if desc.lower() in "encrypt":
        plaintext = input("enter text to encrypt:-")
        key=int(input("enter key:-"))
        encrypted_text = ozp_cipher_encoder.encrypt_text(plaintext,key)
        # print("Original Text:", plaintext)
        print("Encrypted Text:", encrypted_text)
    elif desc.lower() in "decrypt":
        encrypted_text = input("enter text to decrypt:-")
        key=int(input("enter key:-"))
        decrypted_text = ozp_cipher_decoder.decrypt_text(encrypted_text,key)
        # print("Original Text:", plaintext)
        print("Decrypted Text:", decrypted_text)
    else:
        print("some error1")
except:
    print("some error2")
