def add_num(octal_part,key):
    n=len(octal_part)
    octal_part=int(octal_part)
    if key%2==0:
        octalpart+=len(octalpart)*"1"
    else:
        octalpart+=len(octalpart)*"2"
    return octalpart

def encrypt_text(text,key):
    encrypted_text = []
    temp=[]

    for i in text:
        octal_part=str(oct(ord(i)))[2:]
        if len(octal_part)==3:
            encrypted_text.append((octal_part)[::-1])
        elif len(octal_part)==2:
            encrypted_text.append(("0"+octal_part)[::-1])
        else:
            encrypted_text.append("error")

    encrypted_text="".join(encrypted_text)
    encrypted_text=int(encrypted_text)*key*key

    return str(encrypted_text)
