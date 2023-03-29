def encrypt(plain_text,keyword):
    plainC = list(plain_text)
    plain = []
    for i in plainC:
        plain.append(ord(i) - 65)

    keyC = list(keyword)
    key = []
    for i in keyC:
        key.append(ord(i) - 65)

    cipher = []
    for i in range(0,len(plain)):
         sum = plain[i] + key[i % len(key)]
         sum = sum % 26
         cipher.append(chr(sum + 65))

    return("".join(cipher))

def decrypt(cipher_text,keyword):
    cipherC = list(cipher_text)
    cipher = []
    for i in cipherC:
        cipher.append(ord(i)-65)

    keyC = list(keyword)
    key = []
    for i in keyC:
        key.append(ord(i) - 65)

    answer = []
    for i in range(0,len(cipher)):
        diff = cipher[i] - key[i%len(key)]
        diff = diff % 26
        answer.append(chr(diff + 65))

    return "".join(answer)
        

string = "GEEKSFORGEEKS"
string2 = "GCYCZFMLYLEIM"
keyword = "AYUSH"
print("Encrypted text is",encrypt(string,keyword))
print("Decrypted text is",decrypt(string2,keyword))
